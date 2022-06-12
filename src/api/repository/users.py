import os
import re
from typing import List

from fastapi import HTTPException, status

from database.database import connection
from api.models.users import users
from api.schemas.users import User


async def all() -> List[dict]:
    """ Return all users in the database."""
    return await connection.execute(users.select()).fetchall()


async def show_by_id(id: str) -> dict:
    """Return the user by its id."""
    return await connection.execute(users.select().where(users.c.id == id)).first()


async def show_by_name(name: str) -> dict:
    """Return the user by its name."""
    return await connection.execute(users.select().where(users.c.name == name)).first()

async def show_by_cpf(cpf: str, format: bool) -> dict:
    """Return the user by its cpf."""
    if format:
        user = await connection.execute(
            users.select().where(users.c.cpf == cpf)
        ).first()
        cpf = user.pop('cpf')
        user["cpf"] = f"{user.cpf[:3]}." \
                      f"{user.cpf[3:6]}." \
                      f"{user.cpf[6:9]}" \
                      f"-{user.cpf[9:]}"
        return user

    return await connection.execute(
            users.select().where(users.c.cpf == cpf)
        ).first()


async def show_by_birth_date(birth_date: str) -> dict:
    """Return the user by its birth date."""
    return await connection.execute(users.select().where(
        users.c.birth_date == birth_date)
    ).first()


async def show_by_email(email: str) -> dict:
    """Return the user by its email."""
    return await connection.execute(users.select().where(
        users.c.email == email)
    ).first()


async def destroy(id: str) -> dict:
    """Delete the users and return the user deleted."""
    return await connection.execute(users.delete().where(users.c.id == id))


async def create_user(user: User) -> dict:
    """Create a new user"""
    new_user = User(
        id=user.id,
        name=user.name,
        cpf=user.cpf,
        birth_date=user.birth_date,
        email=user.email,
        photo=user.photo
    )

    valid_user = user_update_validation(new_user)

    user_created = await connection.execute(users.insert().values(valid_user))
    return connection.execute(users.select().where(
        users.c.id == user_created.lastrowid)
    ).first()


async def update(id: str, user: User) -> dict:
    """Update a existent user."""
    updated_user = User(
        name=user.name, cpf=user.cpf, birth_date=user.birth_date, email=user.email
    )
    current_user = connection.execute(users.select().where(users.c.id == id)).first()
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found."
        )

    return await connection.execute(users.update().values(updated_user).where(users.c.id == id))


def user_update_validation(user: User) -> users:
    """This function validate if is possible update the user"""
    email_validator = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if str(user.photo) not in ['.png', '.bpm', '.jpeg']:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Unaceptable photo format. "
                   "Please, upload a photo with a valid formats "
                   "(png, bmp or jpeg)."
        )

    if os.stat(user.photo) .st_size > 1000000:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Size Photo is higher than 1Mb."
        )

    if not re.search(email_validator, user.email):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="It is not a valid email."
        )
