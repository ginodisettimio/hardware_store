from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    HOST: str = '127.0.0.1'
    PORT: int = 8000
    DEV: bool = False

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION_TIME_MINUTES: int = 60

    # External Data
    HARDWARE_API: str

    # Database
    DB_CONNECTION: str

    # Logging
    DEBUG: bool = False

    class Config:
        env_file = '.env'
