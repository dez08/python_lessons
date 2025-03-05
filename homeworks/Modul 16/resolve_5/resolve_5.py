# Домашнее задание по теме "Модели данных Pydantic"

from fastapi import FastAPI, status, Body, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
def first_welcome(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/users/{user_id}')
def welcome(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})


@app.post('/user/{username}/{age}')
def welcome_id_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                          age: int = Path(ge=18, le=120, description='Enter Age', example='24')) -> User:
    user_id = len(users) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
def change_id_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='1'),
                         username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                         age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
def del_user(user_id: int = Path(description='Enter User ID', example='1')) -> User:
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail='User was not found')
    users.remove(user)
    return user