from typing import Optional

from fastapi import APIRouter, Response, status
from fastapi_pagination import Page, paginate

from api.schemas.users import User
from api.repository import users

router = APIRouter()


@router.get('/', response_model=Page[User], status_code=status.HTTP_200_OK)
async def users():
    return await paginate(users.all())


@router.get('/{name}', response_model=User, status_code=status.HTTP_200_OK)
async def user_by_name(name: str):
    return users.show_by_name(name)


@router.get('/{cpf}', response_model=User, status_code=status.HTTP_200_OK)
async def user_by_name(cpf: str):
    return users.show_by_cpf(cpf)


@router.get(
    '/{birth_date}',
    response_model=User,
    status_code=status.HTTP_200_OK
)
async def user_by_name(birth_date: str):
    return users.show_by_birth_date(birth_date)


@router.get('/{email}', response_model=User, status_code=status.HTTP_200_OK)
async def user_by_name(email: str):
    return users.show_by_email(email)


@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    return await create_user(user)


@router.put('/{id}')
async def update_user(id: str, user: User):
    return await users.update(id, user)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    return await users.destroy(id)
