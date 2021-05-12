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
from sqlalchemy.ext.asyncio import  create_async_engine, AsyncSession
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

SESSON_COUNTER = 0

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
#PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI,echo = True)
Base = declarative_base()



#для модели User обязательными являются name, username, email
#создайте связи relationship между моделями: User.posts и Post.user
class User(Base):
    __tablename__ = 'Users'
    __mapper_args__ = {'eager_defaults':True}


    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False,server_default='')
    username = Column(String,nullable=False,server_default='')
    email = Column(String,nullable=False,server_default='nowhere@nowhere.com')

    post = relationship('Post',back_populates='user_relate')

#для модели Post обязательными являются user_id, title, body
class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=True,server_default='')
    body = Column(String,nullable=True,server_default='')

    user_id = Column(Integer,ForeignKey(User.id),nullable=False)
    user_relate = relationship("User",back_populates='post')

#Session = None

async def create_tables():
    print('creating tables...')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_user(*args):
    c = 0
    print('args====',*args)
    print('creating users\'s queque')
    async_session = sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)
    async with async_session() as session:
        session : AsyncSession
        async with session.begin():
            # session.add(args[0])
            #print('I am here')
            print('I am args = ', args)
            for u in zip(*args):
                print('I am u = ',u)
                session.add(*u)
                c+=1
        print('added ',c ,' users')
        await session.commit()

async def add_post(post:Post):
    print('adding post')
    async_session = sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)

    async with async_session() as session:
        session : AsyncSession

        async with session.begin():
            session.add(post)
        await session.commit() # commiting

# async def main():
#     await create_tables()
#
# if __name__ == '__main__':
#     asyncio.run(main())
