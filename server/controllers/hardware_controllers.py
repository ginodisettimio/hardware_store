import logging
from typing import List

from server.schemas import NewHardwareRequest, UpdateHardwareRequest, HardwareResponse
from server.exceptions import InternalServerError, BaseHTTPException
from server.services import HardwareService


logger = logging.getLogger(name=__name__)


class HardwareController:

    def __init__(self):
        self.service = HardwareService()

    def create(self, new_product: NewHardwareRequest) -> HardwareResponse:
        try:
            logger.debug(f'Crear producto {new_product.name}')
            return self.service.create(new_product)
        except BaseHTTPException as ex:
            logger.debug(f'Excepción capturada: {type(ex).__name__} - {ex.description}')
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(msg=f'Error no contemplado en {__name__}.create()')
            raise InternalServerError()

    def get_all(self, limit: int, offset: int) -> List[HardwareResponse]:
        try:
            logger.debug(msg=f'Obtener todos los productos')
            return self.service.get_all(limit, offset)
        except BaseHTTPException as ex:
            logger.debug(f'Excepción capturada: {type(ex).__name__} - {ex.description}')
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(msg=f'Error no contemplado en {__name__}.create()')
            raise InternalServerError()

    def get_by_id(self, id: int) -> HardwareResponse:
        try:
            logger.debug(msg=f'Obtener producto id #{id}')
            return self.service.get_by_id(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(msg=f'Error no contemplado en {
                            __name__}.get_by_id()')
            raise InternalServerError()

    def update(self, id: int, product: UpdateHardwareRequest) -> HardwareResponse:
        try:
            logger.debug(msg=f'Actualizar producto {product.name} id #{id}')
            return self.service.update(id, product)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(msg=f'Error no contemplado en {__name__}.update()')
            raise InternalServerError()

    def delete(self, id: int) -> None:
        try:
            logger.debug(msg=f'Eliminar producto id #{id}')
            return self.service.delete(id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception:
            logger.critical(msg=f'Error no contemplado en {__name__}.delete()')
            raise InternalServerError()

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor con status code:{ex.status_code} : {ex.description}')
        else:
            logger.error(f'Error {ex.status_code} : {ex.description}')
        raise ex
