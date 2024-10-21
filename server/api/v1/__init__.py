from fastapi import APIRouter

from server.api.v1.hardware_routes import router

router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(router, tags=['Hardware'])
