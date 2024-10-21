from fastapi import APIRouter

from server.api.v1 import router_v1


router_api = APIRouter(prefix='/api')

router_api.include_router(router_v1)
