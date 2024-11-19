import logging

from server.schemas import RegisterUser, LoginUser, TokenResponse
from server.exceptions import InternalServerError, BaseHTTPException, UniqFieldException, BadRequest
from server.services import AuthService


logger = logging.getLogger(__name__)


class AuthController():

    def __init__(self):
        self.auth_service = AuthService()

    def register(self, new_user: RegisterUser) -> TokenResponse:
        try:
            return self.auth_service.register(new_user)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except UniqFieldException as ex:
            logger.error(str(ex))
            raise BadRequest('Campo username/email duplicado.')
        except Exception as ex:
            logger.critical(msg=f'Error no contemplado en {__name__}.register()' + str(ex))
            raise InternalServerError(str(ex))

    def login(self, credentials: LoginUser) -> TokenResponse:
        try:
            return self.auth_service.login(credentials)
        except BaseHTTPException as ex:
            self.__handler_http_exception(ex)
        except Exception as ex:
            logger.critical(f'Error no contemplado en {__name__}.login(): ' + str(ex))
            raise InternalServerError(str(ex))

    def __handler_http_exception(self, ex: BaseHTTPException):
        if ex.status_code >= 500:
            logger.critical(f'Error en el servidor con status code:{
                            ex.status_code} : {ex.description}')
        else:
            logger.error(f'Error {ex.status_code} : {ex.description}')
        raise ex
