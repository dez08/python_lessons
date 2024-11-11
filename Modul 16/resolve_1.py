# Домашнее задание по теме "Основы Fast Api и маршрутизация

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def welcome_admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def welcome_user(user_id: str) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def welcome_id_user(username: str = 'Unknow', age: int = 0) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'