from sqlalchemy import  Column, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base

from base import Base
from sqlalchemy import event
from sqlalchemy.engine import Engine
#listens for db connections to enforce Foreign key ocnstraints
#generates exception that can be handled
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
class Performance(Base):
    __tablename__ = 'performances'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    locationCity = Column(String)
    locationState = Column(String)


    def __repr__(self):
        return 'Performance: ID: {} Location : {}, {} Date: {}-{}-{}'.format(self.id,
            self.locationCity, self.locationState, self.month, self.day, self.year)
#updates the db schema to enforce foreign key constraints
engine = create_engine('sqlite:///tourMerchManagerDB.db', echo=False)
Base.metadata.create_all(engine)
