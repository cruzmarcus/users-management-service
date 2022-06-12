from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def hello():
    return {'message': 'hello world2'}


@router.get('/a')
async def helloa():
    return {'message': 'hello world'}