from fastapi import FastAPI

from server.api import router_api
from server.database import database_connection, create_tables


hardware = FastAPI()

hardware.include_router(router_api)

if database_connection.connect() is True:
    create_tables()


@hardware.on_event('startup')
async def startup_event():
    database_connection.connect()


@hardware.on_event('shutdown')
async def shutdown_event():
    database_connection.disconnect()
