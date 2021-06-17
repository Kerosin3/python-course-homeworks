from sqlalchemy import Column,Integer,String

from ..models.database import db


class Stock(db.Model):
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False,unique=False,server_default='')
    pe_indexes = Column( Integer,nullable=True,default=0,server_default='0' )
