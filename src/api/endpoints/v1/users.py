from fastapi import APIRouter, Response, status
from fastapi_pagination import Page, paginate

from api.schemas.users import User
from api.repository import users


router = APIRouter()


@router.get('/', response_model=Page[User])
async def users():
    return await paginate(users.all())


@router.get('/{id}')
async def user_id(id: str):
    return users.show(id)


@router.post('/')
async def create_user():
    return await create_user()


@router.post('/')
async def update_user():
    return await users.update()


@router.delete('/{id}')
async def delete_user(id: str):
    return await users.destroy(id)
