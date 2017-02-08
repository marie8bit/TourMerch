from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from base import Base
class Record(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    item = Column(String)
    value = Column(Float)
    quantity = Column(Integer)
    performance = Column(Integer)

    def __repr__(self):
        return 'Sales: ID: {} Item Sold = {} Sales Price = {} Quantity sold = {}'.format(self.id, self.item, self.value, self.quantity)
