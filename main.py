import uvicorn

from server.configs import app_settings as settings


if __name__ == '__main__':
    uvicorn.run('server.app:hardware', host=settings.HOST, port=settings.PORT, reload=settings.DEV)
