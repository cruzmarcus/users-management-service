from fastapi import APIRouter, Depends
from fastapi_pagination import add_pagination
from .v1.users import router

api_router = APIRouter()


api_router.include_router(
    router,
    tags=["Users"],
    prefix="/v1",
)

add_pagination(api_router)
