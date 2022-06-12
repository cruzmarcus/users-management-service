from sqlalchemy import create_engine

from sqlalchemy.orm import registry, sessionmaker

from src.api.models import user
from src import config

settings = config.get_settings()

mapper_registry = registry()

engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

mapper_registry.map_imperatively(user.User, user.users_table)
