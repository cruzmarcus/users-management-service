from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Table

from src.database.database import metadata, engine


@dataclass
class Users:
    id: int
    name: str
    cpf: str
    birth_date: str
    email: str


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(150)),
    Column('cpf', String(11)),
    Column('birth_date', String(10)),
    Column('email', String(255)),
)

metadata.create_all(engine)
