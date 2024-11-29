from fastapi import FastAPI
from fastapi.middleware import Middleware

from server.api import router_api
from server.database import database_connection
from server.middlewares.request_logging_middleware import RequestLoggingMiddleware
from server.middlewares.jwt_middleware import JwtMiddleware


api_middlewares = [
    Middleware(RequestLoggingMiddleware),
    Middleware(JwtMiddleware),
]

hardware = FastAPI(middleware=api_middlewares)

# Incluimos el router principal a la instancia de FastAPI
hardware.include_router(router_api)

# if database_connection.connect() is True:
#     create_tables()


@hardware.on_event('startup')
async def startup_event():
    database_connection.connect()
    if database_connection is True:
        print('\033[92m', 'Connected to Database', '\033[0m')


@hardware.on_event('shutdown')
async def shutdown_event():
    database_connection.disconnect()
