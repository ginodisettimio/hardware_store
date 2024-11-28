import logging
import json
import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

request_logger = logging.getLogger(name='request_logger')


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    SENSITIVE_FIELDS = ['password']

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        # Capturar los datos del request para loggearlos
        initial_time = time.time()
        method = request.method
        url = str(request.url.path)
        client_ip = request.client.host
        query_params = request.query_params
        body_param = await request.body()
        body_param = self.__hide_sensitive_fields(body_param)

        # Durante el endpoint
        response = await call_next(request)

        # Despues del endpoint
        end_time = time.time()
        execution_time = str(end_time - initial_time) + 'ms'
        info_data = f'{client_ip} - "{method} {url}{f"?{query_params}" if query_params else ""}" code={response.status_code} time={execution_time}'
        if body_param:
            info_data += f'\nBODY: {str(body_param)}'
        request_logger.info(info_data)

        return response

    def __hide_sensitive_fields(self, body: bytes) -> str:
        if not body:
            return ''
        try:
            body_json = json.loads(body)
            for field in self.SENSITIVE_FIELDS:
                if field in body_json:
                    body_json[field] = '**********'
            return json.dumps(body_json)
        except json.JSONDecodeError:
            body.decode('utf-8')
