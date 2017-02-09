from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from merchSales import Sale
#from sqlalchemy import ForgeignKey
# @event.listens_for(Engine, "connect")
# def set_sqlite_pragma(dbapi_connection, connection_record):
#     cursor = dbapi_connection.cursor()
#     cursor.execute("PRAGMA foreign_keys=ON")
#     cursor.close()
engine = create_engine('sqlite:///tourMerchManagerDB.db', echo=True)
#Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
from items import Item
from performances import Performance
from base import Base
def setup():
    save_session = Session()
    item1 = Item(description = 'White T-Shirt Logo', value = 25.95 )
    item2 = Item(description = 'White T-Short Photo', value = 25.95)
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

def addNewObject(ObTypeAdd, **keywords):
    save_session = Session()
    if (type(ObTypeAdd) == Item):
        item = Item(description = keywords[description], value = keywords[value])
        save_session.add(item)
    elif (type(obTypeAdd)== Performance):
        perf = Performance(year = keywords[year], month = keywords[month],
            day = keywords[day], locationCity = keywords[locationCity],
            locationState = keywords[locationState])
        save_session.add(perf)
    elif(type(obTypeAdd)== Sale):
        sale = Sale(itemID = keywords[itemID], quantity = keywords[quantity],
            performanceID = keywords[performanceID])
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
