import uvicorn

from server.configs import app_settings as settings


if __name__ == '__main__':
    # No me deja poner el host='0.0.0.0'
    uvicorn.run('server.app:hardware', host='127.0.0.1', port=settings.PORT, reload=settings.DEV)
