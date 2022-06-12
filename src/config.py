import functools

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_ADDRESS: str = 'localhost:8000'
    API_DESCRIPTION: str = "Users management service API"
    API_ROOT_PATH: str = ''
    API_TITLE: str = "Users management service API"
    API_VERSION: str = "1.0.0"
    DATABASE_URL: str = "mysql+asyncmy//root:root@localhost:3306/users"

    class Config:
        env_file = '.env'


@functools.lru_cache(maxsize=16)
def get_settings() -> Settings:
    return Settings()
