from server.exceptions.base_http_exception import BaseHTTPException


class BadRequest(BaseHTTPException):
    description = 'Algo esta mal en la request enviada por el cliente'
    status_code = 400


class NotFound(BaseHTTPException):
    description = 'No se encontró el recurso'
    status_code = 404


class UnproccesableEntity(BaseHTTPException):
    description = 'El servidor no fue capaz de ejecutar las intrucciones requeridas'
    status_code = 422
