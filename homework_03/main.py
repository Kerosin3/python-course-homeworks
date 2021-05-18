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
from models import User,Post,create_tables
import asyncio,random,string
from jsonplaceholder_requests import get_jsonS

async def async_main_v3():
    await create_tables()
    list_users =[]
    list_posts = []
    for i in range(3): # creating several users
        user = create_a_user()
        list_users.append(user)
        list_posts.append(create_posts_for_a_user(user=user))
    #list_posts = [item for sublist in list_posts for item in sublist] # flatten
    print('users=',list_users)
    print('posts=',list_posts)
    res = await asyncio.gather(
        add_user(*list_users),
        #add_post(*list_posts)
    )
    print('res=', res)
async def async_main():
    await create_tables()
def create_n_users(n_users:int)-> list[User]:
    list_users = []
    for i in range(n_users):
        list_users.append(get_name_username())
    print('list_users', list_users)
    return list_users

def create_a_user():
    return get_name_username()

def get_name_username() -> User:
    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    nickname = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    print(f'created user with name:{name},and username:{nickname}')
    return User(name=name,username=nickname)

def create_posts_for_a_user(user:User)-> list[Post]:
    posts = []
    for j in range(random.randint(1, 5)):  # creating random posts for a user
        potinfo = 'post '+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3,7))
        posts.append(Post(title=str(user.name)+'\'s'+ ' title', body=potinfo, user_relate=user))
    return posts


if __name__ == "__main__":
    asyncio.run(async_main_v3())
