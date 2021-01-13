from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateUserDto
from api.response import ResponseGetUserDto
from transport.sanic.endpoints import BaseEndpoint

from db.queries import user as user_queries


# Endpoint для обработки запроса на создание пользователя
class CreateUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        # DTO объект
        request_model = RequestCreateUserDto(body)

        # экземпляр базы данных
        db_user = user_queries.create_user(session, request_model)
        session.commit_session()

        # процесс валидации, создание модели response model
        response_model = ResponseGetUserDto(db_user)

        return await self.make_response_json(body=response_model.dump(), status=201)
