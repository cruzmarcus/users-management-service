from sqlalchemy import create_engine, MetaData

from src import config

settings = config.get_settings()

metadata = MetaData()


engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

connection = engine.connect()

