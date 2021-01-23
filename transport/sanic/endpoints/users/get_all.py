from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response import ResponseGetUserDto

from db.database import DBSession
from db.queries import user as user_queries

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicAuthException


class AllUsersEndpoint(BaseEndpoint):

    async def method_get(
            self, request: Request, body: dict, session: DBSession, *args, **kwargs
    ) -> BaseHTTPResponse:

        # проверяем, что пользователь не удален из базы (is_deleted != 1)
        if user_queries.get_user(session=session, user_id=body['id']).is_deleted:
            raise SanicAuthException('Not authenticated')

        db_user = user_queries.get_users(session)

        response_model = ResponseGetUserDto(db_user, many=True)

        return await self.make_response_json(
            status=200, body=response_model.dump()
        )
