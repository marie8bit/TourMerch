from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from merchSales import Sale
from items import Item
import ui
from performances import Performance
from base import Base

engine = create_engine('sqlite:///tourMerchManagerDB.db', echo=False)

Session = sessionmaker(bind=engine)

def setup():
    #adds items to the items table
    save_session = Session()
    item1 = Item(description = 'White T-Shirt Logo', value = 25.95 )
    item2 = Item(description = 'White T-Shirt Photo', value = 25.95)
    item3 = Item(description = 'Concert DVD', value = 34.95)
    item4 = Item(description = 'Album 2016', value = 15.99)
    for item in [item1, item2, item3, item4]:
        #ckecks that the item doesn't already exist before adding it again
        if not (getItem(item.description)):
            save_session.add(item)
    save_session.commit()
    save_session.close()
#returns a list of objects to the function that called it
#takes object type as an argument so it can handle all table queries
def showAll(ObType):
    search_session = Session()
    obList = search_session.query(ObType).all()
    search_session.close()
    return obList
#adds objects to the database can process all classes in program
#accepts validated data
def addNewObject(ObTypeAdd, *args):
    save_session = Session()
    argList=[]
    #converts arguments into a list for processing args by list index
    for arg in args:
        argList.append(arg)
    if (ObTypeAdd == 'Item'):
        item = Item(description = argList[0], value = argList[1])
        save_session.add(item)
    elif (ObTypeAdd == 'Performance'):
        perf = Performance(year = argList[0], month = argList[1], day = argList[2],
            locationCity = argList[3], locationState = argList[4])
        save_session.add(perf)
    elif(ObTypeAdd == 'Sale'):
        sale = Sale(itemID = argList[0], quantity = argList[1], performanceID = argList[2])
        save_session.add(sale)
    save_session.commit()
    save_session.close()
#checks if an item is present in the database
def getItem(string):
    search_session=Session()
    count = search_session.query(Item).filter_by(description = string).count()
    if (count >0):
        search_session.close()
        return True
    else:
        search_session.close()
        return False
#returns an item or a performance object from the database
def getObjectByID(objectTypeStr, aid):

    search_session=Session()
    while True:
        if (objectTypeStr == 'Item'):
            try:
                #uses one beacuse it is querying by primary key
                item = search_session.query(Item).filter_by(id = aid).one()
                break
            except exc.SQLAlchemyError:
                #loops until it gets valid input
                aid = ui.getPositiveInt(input('Please enter an ID from the list: '))
        elif (objectTypeStr == 'Performance'):
            try:
                item = search_session.query(Performance).filter_by(id = aid).one()
                break
            except exc.SQLAlchemyError:
                aid = ui.getPositiveInt(input('Please enter an ID from the list: '))

    search_session.close()
    return item
#calculates the total sales
def getSalesByID(iID):
    search_session = Session()
    #gets item from database to access items value/validates user input
    item = getObjectByID('Item', iID)
    #gets all instances of sales that have received itemid as attribute
    itemSales = search_session.query(Sale).filter_by(itemID = item.id).all()
    total = 0
    for sale in itemSales:
        #item value stays the same for each sale object in list
        total += sale.quantity * item.value
    print ('Total sales for '+item.description+':')
    print ('$'+str(round(total, 2)))
    search_session.close()
#calulates teh total sales by validated performanceID
def getSalesByPerf(pID):
    search_session = Session()
    #vaildates user input to handle potential database query errors
    perf = getObjectByID('Performance', pID)
    #gets all sales instances with received performanceID as attribute
    #uses perf incase passed argument is no longer applicable after data validation
    perfSales = search_session.query(Sale).filter_by(performanceID = perf.id).all()
    total = 0
    for sale in perfSales:
        #gets item as item is as there may be many different items sold as one performance
        item = search_session.query(Item).filter_by(id = sale.itemID).one()
        total += sale.quantity * item.value
    print ('Total sales for this performance:')
    print ('$'+str(round(total, 2)))
