"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import asyncio,os
from sqlalchemy.ext.asyncio import  create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import (
    declarative_base,
    joinedload,
    selectinload, relationship,sessionmaker
)
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    func
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI,echo = True)
Base = declarative_base()



#для модели User обязательными являются name, username, email
#создайте связи relationship между моделями: User.posts и Post.user
class User():
    __tablename__ = 'Users'


    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False,server_default='')
    username = Column(String,nullable=False,server_default='')
    email = Column(String,nullable=False,server_default='nowhere@nowhere.com')

    post = relationship('Post',back_populates='user_relate')

#для модели Post обязательными являются user_id, title, body
class Post():
    __tablename__ = 'Posts'

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=True,server_default='')
    body = Column(String,nullable=True,server_default='')
    user_id = Column(Integer,ForeignKey(User.id),nullable=False)
    user_relate = relationship("User",back_populates='post')

Session = None
