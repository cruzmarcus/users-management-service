from fastapi import FastAPI
from api.endpoints.router import api_router
import config

settings = config.get_settings()

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    openapi_tags=[{
        "name": "users",
        "description": "CRUD users datas"
    }]
)

app.include_router(api_router)
