from sqlalchemy import Column, Integer, String
from .database import db

#implement foreignkey feature

class Stock_db(db.Model):
    # __tablename__ = 'Stocks'
    # __mapper_args__ = {'eager_defaults',True}
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, server_default='')
    price = Column(Integer, nullable=True, unique=False, server_default='0')
    # prices = relationship('Prices',back_populates='pe_indexes')


def gen_stock_db() -> Stock_db:
    return Stock_db()


def test_me_models():
    return True
#
# class Prices(db.Model):
#     __tablename__ = 'Prices'
#
#     id = Column(Integer,primary_key=True)
#     stock_name = Column(String,nullable=False,unique=False,server_default='')
#
#     pe_indexes = Column( Integer,nullable=True,default=0,server_default='0')
