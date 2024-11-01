import logging

import requests

from server.configs import app_settings


logger = logging.getLogger(name=__name__)

class HardwareApi:
    def __init__(self) -> None:
        self.client = requests.Session()
        self.base_url = app_settings.HARDWARE_API

    def get_all(self, limit: int, offset: int):
        url = self.base_url + '/products'
        params = {
            'limit': limit,
            'offset': offset,
        }
        response = self.client.get(url=url, params=params)
        logger.info(f'[GET] {response.url}: {response.status_code}')

        return response.json
