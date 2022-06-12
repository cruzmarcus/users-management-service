from dataclasses import dataclass, field

from sqlalchemy import Column, Integer, MetaData, String, Table


@dataclass
class User:
    id: int = field(init=False)
    name: str
    cpf: str
    birth_date: str
    email: str


metadata = MetaData()

users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(150)),
    Column('cpf', String(11)),
    Column('birth_date', String(10)),
    Column('email', String(255)),
)
