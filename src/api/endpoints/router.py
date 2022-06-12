from fastapi import APIRouter, Depends
from api.endpoints.v1.users import router

api_router = APIRouter()


api_router.include_router(
    router,
    tags=["Users"],
    prefix="/v1",
)
