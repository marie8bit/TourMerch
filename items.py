from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from merchSales import Sale
from base import Base
from sqlalchemy import event
from sqlalchemy.engine import Engine
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    value = Column(Float)


    def __repr__(self):
        return 'Item: ID: {} Description = {} Sales Price = {} '.format(self.id, self.description, self.value)
engine = create_engine('sqlite:///tourMerchManagerDB.db', echo=True)
Base.metadata.create_all(engine)
