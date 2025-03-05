# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/')
async def first_welcome() -> str:
    return 'Hello World'


@app.get('/users')
async def welcome() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def welcome_id_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                          age: int = Path(ge=18, le=120, description='Enter Age', example='24')) -> str:
    user_id = str(int(max(users,key=int))+1)
    users[user_id] = f'Имя: {username}, возраст {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def change_id_user(user_id: int = Path(ge=1, le=100,description='Enter User ID', example='1'),
                         username: str = Path(min_length=5,max_length=20, description= 'Enter username', example='UrbanUser'),
                         age: int = Path(ge=18, le=120,description='Enter age', example='24')) -> str:
    users[user_id] = f'Имя: {username}, возраст {age}'
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def del_user(user_id: int = Path(ge=1, le=100,description='Enter User ID', example='1')) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'
