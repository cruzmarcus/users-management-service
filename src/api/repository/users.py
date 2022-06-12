from typing import List

from database.database import connection
from api.models.users import users
from api.schemas.users import User


async def all() -> List[dict]:
    """ Return all users in the database."""
    return await connection.execute(users.select()).fetchall()


async def show(id: str) -> dict:
    """Return the user by its id."""
    return await connection.execute(users.select().where(users.c.id == id)).first()


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
        email=user.email
    )
    result = await connection.execute(users.insert().values(new_user))
    return connection.execute(users.select().where(
        users.c.id == result.lastrowid)
    ).first()


async def update(id: str, user: User) -> dict:
    """Update a existent user."""
    updated_user = User(
        name=user.name, cpf=user.cpf, birth_date=user.birth_date, email=user.email
    )
    await connection.execute(users.update().values(updated_user).where(users.c.id == id))
    return connection.execute(users.select().where(users.c.id == id)).first()
