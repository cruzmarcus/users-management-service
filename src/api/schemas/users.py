from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    """Definition attribute model User"""
    id: Optional[str]
    name: str
    cpf: str
    birth_date: str
    email: str
    photo: str

    class Config:
        orm_mode = True
