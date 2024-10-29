from typing import List

from server.schemas.hardware_schemas import NewHardwareRequest, UpdateHardwareRequest, HardwareResponse
from server.exceptions.server_exceptions import InternalServerError
from server.exceptions.base_http_exception import BaseHTTPException
from server.services.hardware_services import HardwareService


class HardwareController:
    def __init__(self):
        self.service = HardwareService()

    def create(self, new_product: NewHardwareRequest) -> HardwareResponse:
        try:
            return self.service.create(new_product)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError('')

    def get_all(self, limit: int, offset: int) -> List[HardwareResponse]:
        try:
            return self.service.get_all(limit, offset)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def get_by_id(self, id: int) -> HardwareResponse:
        try:
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def update(self, id: int, product: UpdateHardwareRequest) -> HardwareResponse:
        try:
            return self.service.update(id, product)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            return self.service.delete(id)
        except BaseHTTPException as ex:
            raise ex
        except Exception:
            raise InternalServerError()
