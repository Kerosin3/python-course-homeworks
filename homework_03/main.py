from jsonplaceholder_requests import get_jsonS,users,posts,parse_posts,parse_users
from models import create_tables,Session
import asyncio
from sqlalchemy.ext.asyncio import  create_async_engine, AsyncSession


async def async_main():
    await create_tables()
    users_list = await get_jsonS(users)
    posts_list = await get_jsonS(posts)
    usersZ=parse_users(users_list)
    postsZ=parse_posts(posts_list)
    await add_info(usersZ)
    await add_info(postsZ)


async def add_info(input:list):
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

def main():
    asyncio.run(async_main())

# async def async_main():
#     pass

if __name__ == '__main__':
    main()
