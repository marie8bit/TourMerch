from sqlalchemy import  Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from base import Base
class Performance(Base):
    __tablename__ = 'performances'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    locationCity = Column(String)
    locationState = Column(String)


    def __repr__(self):
        return 'Performance: ID: {} Location : {} Date: {}-{}-{}'.format(self.id, self.location, self.month, self.day, self.year)
