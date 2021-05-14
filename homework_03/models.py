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
import random

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

    def __repr__(self):
        return f"my name is {self.name},my username is {self.username}"
        #return f"{self.name}"
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


async def add_user(in_list:list[User]):
    c = 0
    print('creating users\'s queque')
    async_session = sessionmaker(engine,class_=AsyncSession,expire_on_commit=False)
    async with async_session() as session:
        session : AsyncSession
        async with session.begin():
            admin = User(name='Admin',username='Admin')
            post = Post(title='admin_post_title', body='admin_post_body', user_relate=admin)
            session.add(admin,post)
            for u in in_list:
            #for u in zip(*args):
                posts = []
                # postx = Post(title='some_titile', body='some_body', user_relate=u)
                for j in range(random.randint(1,5)):
                    posts.append(Post(title='some_titile', body='some_body', user_relate=u))
                session.add(u)
                session.add_all(posts)
                c+=1
        print('added ',c ,' users')
        print('Finishing session')
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
