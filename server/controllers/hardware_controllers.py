import logging
from typing import List

from server.schemas import NewHardwareRequest, UpdateHardwareRequest, HardwareResponse
from server.exceptions import InternalServerError, BaseHTTPException
from server.services import HardwareService


logger = logging.getLogger(__name__)


class HardwareController:

    def __init__(self):
        self.service = HardwareService()

    def create(self, new_product: NewHardwareRequest) -> HardwareResponse:
        try:
            logger.debug(f'Crear producto {new_product.name}')
            return self.service.create(new_product)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.create()')
            raise InternalServerError(str(ex))

    def get_all(self, limit: int, offset: int) -> List[HardwareResponse]:
        try:
            logger.debug(msg=f'Obtener todos los productos')
            return self.service.get_all(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.get_all()')
            raise InternalServerError(str(ex))

    def get_by_id(self, product_id: int) -> HardwareResponse:
        try:
            logger.debug(msg=f'Obtener producto id #{product_id}')
            return self.service.get_by_id(product_id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.get_by_id()')
            raise InternalServerError(str(ex))

    def update(self, product_id: int, product: UpdateHardwareRequest) -> HardwareResponse:
        try:
            logger.debug(msg=f'Actualizar producto {product.name} id #{product_id}')
            return self.service.update(product_id, product)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.update()')
            raise InternalServerError(str(ex))

    def delete(self, product_id: int) -> None:
        try:
            logger.debug(msg=f'Eliminar producto id #{product_id}')
            return self.service.delete(product_id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.delete()')
            raise InternalServerError(str(ex))

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor con status code:{ex.status_code} : {ex.description}')
        else:
            logger.error(f'Error {ex.status_code} : {ex.description}')
        raise ex
