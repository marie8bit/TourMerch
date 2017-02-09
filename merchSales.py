from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import performances
from base import Base
class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    #identifies the relationship between sales and items from the items table
    itemID = Column(Integer, ForeignKey('items.id'))
    quantity = Column(Integer)
    #identifies the relationship between sales and performances
    performanceID = Column(Integer, ForeignKey('performances.id'))

    def __repr__(self):
        return 'Sales: ID: {} Item Sold = {} Quantity sold = {}'.format(self.id,
            self.item, self.quantity)
