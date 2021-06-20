from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship

# from ..models.database import db
from .database import db

class Stock_db(db.Model):
    # __tablename__ = 'Stocks'
    # __mapper_args__ = {'eager_defaults',True}
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False,unique=False,server_default='')
    price = Column(Integer,nullable=True,unique=False,server_default='0')
    # prices = relationship('Prices',back_populates='pe_indexes')

#
# class Prices(db.Model):
#     __tablename__ = 'Prices'
#
#     id = Column(Integer,primary_key=True)
#     stock_name = Column(String,nullable=False,unique=False,server_default='')
#
#     pe_indexes = Column( Integer,nullable=True,default=0,server_default='0')
