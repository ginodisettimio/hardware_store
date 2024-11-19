from server.exceptions.base_http_exception import BaseHTTPException


class BadRequest(BaseHTTPException):
    description = 'Algo esta mal en la request enviada por el cliente'
    status_code = 400


class Unauthorized(BaseHTTPException):
    description = 'El usuario debe estar logueado'
    status_code = 401


class Forbidden(BaseHTTPException):
    description = 'El usuario no puede acceder a este recurso'
    status_code = 403


class NotFound(BaseHTTPException):
    description = 'No se encontro el recurso'
    status_code = 404


class UnproccesableEntity(BaseHTTPException):
    description = 'Algo fallo en la request'
    status_code = 422
