from jsonplaceholder_requests import get_jsonS, users, posts, parse_posts, parse_users
from models import create_tables, Session
import asyncio, os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from models import User,Post
from sqlalchemy.sql import select
from sqlalchemy.orm import selectinload,joinedload


async def async_main():
    await create_tables()
    users_list = await get_jsonS(users)
    posts_list = await get_jsonS(posts)
    usersZ = parse_users(users_list)
    postsZ = parse_posts(posts_list)
    await add_info(usersZ)
    await add_info(postsZ)
    #await get_posts_from_a_user(id=5) # test users and post getting


async def add_info(input: list):
    some_session = Session()
    count = 0
    async with some_session as session:
        session: AsyncSession
        async with session.begin():
            for item in input:
                session.add(item)
                count += 1
        print(f'added {count} entities')
        await session.commit()

async def get_posts_from_a_user(id:int) -> list:
    some_session = Session()
    user_and_posts = []
    posts = []
    c = 0
    async with some_session as session:
        result = await session.execute(select(User).
                                       where(User.id == id).options(selectinload(User.posts)))
        result2 = await session.execute(select(Post).
                                        where(Post.user_id == id).
                                        options(joinedload(Post.user)))
    for i in result:
        user_and_posts.append(*i) #append the user
    for j in result2:
        posts.append(j)
        c += 1
    user_and_posts.append(posts)
    #print('total number of posts:',c)
    return user_and_posts
    #print('posts are',posts)



def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    main()
