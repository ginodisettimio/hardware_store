from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    API: str = '127.0.0.1'
    PORT: int = 8000
    DEV: bool = False

    # External Data
    HARDWARE_API: str

    # Database
    DB_CONNECTION: str

    # Logging
    DEBUG: bool = False

    class Config:
        env_file = '.env'
