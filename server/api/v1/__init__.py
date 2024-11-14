from fastapi import APIRouter

from server.api.v1.hardware_routes import router as hardware_router
from server.api.v1.users_routes import router as user_router
from server.api.v1.auth_routes import router as auth_router


router_v1 = APIRouter(prefix='/v1')

router_v1.include_router(hardware_router, tags=['Hardware'])
router_v1.include_router(user_router, tags=['Users'])
router_v1.include_router(auth_router, tags=['Auth'])
