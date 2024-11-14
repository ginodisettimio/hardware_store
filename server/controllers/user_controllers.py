import logging
from typing import List

from server.schemas import NewUserRequest, UpdateUserRequest, UserResponse
from server.exceptions import InternalServerError, BaseHTTPException, UniqFieldException, BadRequest
from server.services import UsersService


logger = logging.getLogger(__name__)


class UsersController:

    def __init__(self):
        self.service = UsersService()

    def create(self, new_user: NewUserRequest) -> UserResponse:
        try:
            logger.debug(f'Crear usuario {new_user.username}')
            return self.service.create(new_user)
        except BaseHTTPException as ex:
            logger.error(f'Error al procesar request, status code {ex.status_code} : {ex.description}')
            self.__handler_http_exception(ex)
        except UniqFieldException as ex:
            logger.error(str(ex))
            raise BadRequest('Campo username/email duplicado.')
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.create()' + str(ex))
            raise InternalServerError(str(ex))

    def get_all(self, limit: int, offset: int) -> List[UserResponse]:
        try:
            logger.debug(msg=f'Obtener todos los usuarios')
            return self.service.get_all(limit, offset)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.get_all()' + str(ex))
            raise InternalServerError(str(ex))

    def get_by_id(self, user_id: int) -> UserResponse:
        try:
            logger.debug(msg=f'Obtener usuario id #{user_id}')
            return self.service.get_by_id(user_id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.get_by_id()' + str(ex))
            raise InternalServerError(str(ex))

    def update(self, user_id: int, user: UpdateUserRequest) -> UserResponse:
        try:
            logger.debug(msg=f'Actualizar usuario {user.username} id #{user_id}')
            return self.service.update(user_id, user)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.update()' + str(ex))
            raise InternalServerError(str(ex))

    def delete(self, user_id: int) -> None:
        try:
            logger.debug(msg=f'Eliminar usuario id #{user_id}')
            return self.service.delete(user_id)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.delete()' + str(ex))
            raise InternalServerError(str(ex))

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor con status code:{ex.status_code} : {ex.description}')
        else:
            logger.error(f'Error {ex.status_code} : {ex.description}')
        raise ex
