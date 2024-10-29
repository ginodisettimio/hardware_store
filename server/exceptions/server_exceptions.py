from server.exceptions.base_http_exception import BaseHTTPException


class InternalServerError(BaseHTTPException):
    description = 'Error no manejado'
    status_code = 500


class NotImplemented(BaseHTTPException):
    description = 'Funcionalidad no implementada'
    status_code = 501
