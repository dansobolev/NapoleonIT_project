# базовый класс для уровня endpoint'ов

from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.exceptions import ValidationException
from transport.sanic.base import SanicEndpoint


class BaseEndpoint(SanicEndpoint):

    async def _method(self, request: Request, body: dict, *args, **kwargs) -> BaseHTTPResponse:

        # получаем объект database
        database = self.context.database
        session = database.make_session()

        # проводим обработку ошибок валидации в любом методе
        try:
            return await super()._method(request, body, session, *args, **kwargs)
        except ValidationException as error:
            return await self.make_response_json(status=error.status_code, message=str(error))
