from pydantic import BaseModel


class User(BaseModel):
    """Definition attribute model User"""

    name: str
    cpf: str
    birth_date: str
    email: str

    class Config:
        orm_mode = True
