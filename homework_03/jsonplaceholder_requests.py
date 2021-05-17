"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession
import asyncio
import json
from models import User,Post
class Data0:
    def __init__(self,type:str,url:str):
        self.type = type
        self.url = url
    def __repr__(self):
        return f'my type is {self.type},my url is:{self.url}'

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

users = Data0(type='users',url=USERS_DATA_URL)
posts = Data0(type='posts',url=POSTS_DATA_URL)

async def get_response(client: ClientSession,url:str)-> dict:
    async with client.get(url) as resp:
        assert resp.status == 200 # ok
        return await resp.json() # returning json

async def get_jsonS(data_raw:Data0): # accepting Data0 type
    async with ClientSession() as session:
        result = await get_response(session,data_raw.url)
    print('Success')
    print('data fetched:',data_raw.url,data_raw.type,result)
    return result #list of dict

async def main_test():
    users_list = await get_jsonS(users)
    posts_list = await get_jsonS(posts)

    print(parse_users(users_list))
    print(parse_posts(posts_list))


def parse_users(input:dict):
    list_users = []
    for j in input:
        temp = User
        temp.id = j['id']
        temp.username = j['username']
        temp.email = j['email']
        list_users.append(temp)
    return list_users

def parse_posts(input:dict):
    list_posts = []
    for j in input:
        temp = Post
        temp.id = j['id']
        temp.user_id = j['userId']
        temp.title = j['title']
        temp.body = j['body']
        list_posts.append(temp)
    return list_posts
if __name__ == '__main__':
    asyncio.run(main_test())
