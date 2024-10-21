from fastapi import APIRouter

router = APIRouter(prefix='/hardware')


@router.get('/')
async def get_all():
    return []


@router.post('/')
async def create():
    return {}
