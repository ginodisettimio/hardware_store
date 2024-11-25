import logging
from typing import List

from server.schemas import NewHardwareRequest, UpdateHardwareRequest, HardwareResponse, BuyedHardwareResponse, DecodedJwt
from server.exceptions import InternalServerError, BaseHTTPException
from server.services import HardwareService
from server.enums import ADMIN_ROLES
from server.exceptions import Forbidden


logger = logging.getLogger(__name__)


class HardwareController:

    def __init__(self):
        self.service = HardwareService()

    def create(self, new_product: NewHardwareRequest, user_id: int) -> HardwareResponse:
        try:
            logger.debug(f'Crear producto {new_product.name}')
            return self.service.create(new_product, user_id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.create()')
            raise InternalServerError(str(ex))

    def get_list(self, limit: int, offset: int) -> List[HardwareResponse]:
        try:
            logger.debug(msg=f'Obtener todos los productos')
            return self.service.get_list(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {
                __name__}.get_list()')
            raise InternalServerError(str(ex))

    def get_buyed_products_list(self, limit: int, offset: int, token: DecodedJwt) -> List[BuyedHardwareResponse]:
        try:
            logger.debug(msg=f'Obtener lista de compras del usuario')
            return self.service.get_buyed_products_list(limit, offset, token)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {
                            __name__}.get_buyed_products_lis()')
            raise InternalServerError(str(ex))

    def get_by_id(self, product_id: int, token: DecodedJwt) -> BuyedHardwareResponse:
        try:
            logger.debug(msg=f'Obtener producto id #{product_id}')
            product = self.service.get_by_id(product_id)
            self.__check_access(product.user_id, token)
            return product
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {
                            __name__}.get_by_id()')
            raise InternalServerError(str(ex))

    def update(self, product_id: int, product: UpdateHardwareRequest, token: DecodedJwt) -> BuyedHardwareResponse:
        try:
            logger.debug(msg=f'Actualizar producto {
                         product.name} id #{product_id}')
            self.__check_access(product.user_id, token)
            return self.service.update(product_id, product)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.update()')
            raise InternalServerError(str(ex))

    def delete(self, product_id: int, token: DecodedJwt) -> None:
        try:
            logger.debug(msg=f'Eliminar producto id #{product_id}')
            self.get_by_id(product_id, token)
            return self.service.delete(product_id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.delete()')
            raise InternalServerError(str(ex))

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor con status code:{
                            ex.status_code} : {ex.description}')
        else:
            logger.error(f'Error {ex.status_code} : {ex.description}')
        raise ex

    def __check_access(self, owner_id: int, token: DecodedJwt) -> None:
        if (token.user_id != owner_id) and (token.role not in ADMIN_ROLES):
            raise Forbidden('El usuario no es el comprador de este producto.')
