from .settings import Settings
from .logging import config_logger

app_settings = Settings()
config_logger(debug_level=app_settings.DEBUG)
