from datetime import datetime, timedelta

import jwt

from server.configs import app_settings


class JWTHandler():
    
    def __init__(self):
        self.secret_key: str = app_settings
        self.algorithm: str = app_settings.JWT_ALGORITHM
        self.expiration_delta = timedelta(minutes=app_settings.JWT_EXPIRATION_TIME_MINUTES)

    def encode(self, data: dict) -> str:
        payload = data.copy()
        expiration = datetime.now() + self.expiration_delta
        payload.update(exp=expiration)
        return jwt.encode(payload, self.secret_key, self.algorithm)
    
    def decode(self, token: str):
        pass
