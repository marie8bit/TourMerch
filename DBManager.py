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
#from sqlalchemy import ForgeignKey
# @event.listens_for(Engine, "connect")
# def set_sqlite_pragma(dbapi_connection, connection_record):
#     cursor = dbapi_connection.cursor()
#     cursor.execute("PRAGMA foreign_keys=ON")
#     cursor.close()
engine = create_engine('sqlite:///tourMerchManagerDB.db', echo=False)
#Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def setup():
    save_session = Session()
    item1 = Item(description = 'White T-Shirt Logo', value = 25.95 )
    item2 = Item(description = 'White T-Shirt Photo', value = 25.95)
    item3 = Item(description = 'Concert DVD', value = 34.95)
    item4 = Item(description = 'Album 2016', value = 15.99)
    for item in [item1, item2, item3, item4]:
        if not (getItem(item.description)):
            save_session.add(item)
    save_session.commit()
    save_session.close()

def showAll(ObType):
    search_session = Session()
    for ob in search_session.query(ObType).all():
        print(ob)
    search_session.close()

def addNewObject(ObTypeAdd, *args):
    save_session = Session()
    argList=[]
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
def getItem(string):
    search_session=Session()
    count = search_session.query(Item).filter_by(description = string).count()
    if (count >0):
        search_session.close()
        return True
    else:
        search_session.close()
        return False
def getObjectByID(objectTypeStr, aid):

    search_session=Session()
    while True:
        if (objectTypeStr == 'Item'):
            try:
                item = search_session.query(Item).filter_by(id = aid).one()
                break
            except exc.SQLAlchemyError:
                aid = ui.getPositiveInt(input('Please enter an ID from the list'))
        elif (objectTypeStr == 'Performance'):
            try:
                item = search_session.query(Performance).filter_by(id = aid).one()
                break
            except exc.SQLAlchemyError:
                aid = ui.getPositiveInt(input('Please enter an ID from the list'))

    search_session.close()
    return item
def getSalesByID(iID):
    search_session = Session()
    item = search_session.query(Item).filter_by(id = iID).one()
    itemSales = search_session.query(Sale).filter_by(itemID = iID).all()
    total = 0
    for sale in itemSales:
        total += sale.quantity * item.value
    print ('Total sales for '+item.description+':')
    print ('$'+str(round(total, 2)))
    search_session.close()
def getSalesByPerf(pID):
    search_session = Session()
    perfSales = search_session.query(Sale).filter_by(performanceID = pID).all()
    total = 0
    for sale in perfSales:
        item = search_session.query(Item).filter_by(id = sale.itemID).one()
        total += sale.quantity * item.value
    print ('Total sales for this performance:')
    print ('$'+str(round(total, 2)))
