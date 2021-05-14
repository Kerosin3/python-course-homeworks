"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from models import User,Post,create_tables,add_user,add_post
import asyncio,random,string

async def async_main():
    await create_tables()
    list_coroutines = []
    for i in range(10):
        #list_coroutines.append(get_name_username()) # User's list
        list_coroutines.append(add_user(await get_name_username()))
    #print('list_coroutines',list_coroutines)
    res = await asyncio.gather(
        *list_coroutines
    )
    print('res=',res)

async def async_main_v2():
    await create_tables()
    await add_user(await create_n_users(5))
    #await add_post(Post(title='title',body='body',user_relate=''))

async def create_n_users(n_users:int):
    list_users = []
    for i in range(n_users):
        list_users.append(await get_name_username())
    print('list_users', list_users)
    return list_users


async def get_name_username() -> User:
    time_to_sleep = random.random()
    print('sleeping ',time_to_sleep,' seconds')
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    nickname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    print(f'creating user with name:{name},and username:{nickname}')
    await asyncio.sleep(time_to_sleep)
    return User(name=name,username=nickname)


# def get_name_username()-> (str,str):
#     name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
#     nickname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
#     return (name,nickname)

def main():
    pass

def creating_n_users(n:int):
    users = []
    posts = []
    for i in range(n):
        name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        nickname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        user = User(name=name,username=nickname)
        users.append(user)

        post = Post(
            title='some title',
            body='some information',
            user_relate=user
        )
        posts.append(post)
    return  users,posts

if __name__ == "__main__":
    asyncio.run(async_main_v2())
