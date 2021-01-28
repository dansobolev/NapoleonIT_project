from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestGetUserByLoginDto
from api.response import ResponseGetUserByLoginDto

from db.database import DBSession
from db.queries import user as user_queries
from db.exceptions import DBUserNotFoundException, DBUserDeletedException

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserNotFoundException, SanicUserDeletedException


class GetUserByLoginEndpoint(BaseEndpoint):

    async def method_get(
            self, request: Request, body: dict, session: DBSession, user_login, *args, **kwargs
    ) -> BaseHTTPResponse:

        # DTO объект
        request_model = RequestGetUserByLoginDto({'login': user_login})

        try:
            user_info = user_queries.get_user(session, login=request_model.login)
        except DBUserNotFoundException:
            raise SanicUserNotFoundException('User not found')
        except DBUserDeletedException:
            raise SanicUserDeletedException('User deleted')

        response_model = ResponseGetUserByLoginDto(user_info)

        return await self.make_response_json(
            body=response_model.dump(),
            status=200,
        )
