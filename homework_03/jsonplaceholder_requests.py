"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession
import asyncio
from models import User, Post
from dataclasses import dataclass

@dataclass
class data_storage:
    type : str
    url : str

    def __repr__(self):
        return f'my type is {self.type},my url is:{self.url}'


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

users = data_storage(type='users', url=USERS_DATA_URL)
posts = data_storage(type='posts', url=POSTS_DATA_URL)


async def get_response(client: ClientSession, url: str) -> dict:
    async with client.get(url) as resp:
        assert resp.status == 200  # ok
        return await resp.json()  # returning json


async def getting_data_from_remote(data_raw: data_storage):  # accepting data_storage type
    async with ClientSession() as session:
        result = await get_response(session, data_raw.url)
    print('Success getting json')
    print('data fetched:', data_raw.url, data_raw.type, 'result=', result)
    return result  # list of dict


def parse_users(input: dict):
    list_users = []
    for j in input:
        temp = User()
        temp.id = j['id']
        temp.name = j['name']
        temp.username = j['username']
        temp.email = j['email']
        list_users.append(temp)
    return list_users


def parse_posts(input: dict):
    list_posts = []
    for j in input:
        temp = Post()
        temp.id = j['id']
        temp.user_id = j['userId']
        temp.title = j['title']
        temp.body = j['body']
        list_posts.append(temp)
    return list_posts
