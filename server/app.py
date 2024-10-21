from fastapi import FastAPI

from server.api import router_api

hardware = FastAPI()

hardware.include_router(router_api)
