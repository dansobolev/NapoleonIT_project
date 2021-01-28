from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response import ResponseGetUserDto

from db.database import DBSession
from db.exceptions import DBUserDeletedException
from db.queries import user as user_queries

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserDeletedException


class AllUsersEndpoint(BaseEndpoint):

    async def method_get(
            self, request: Request, body: dict, session: DBSession, token: dict, *args, **kwargs
    ) -> BaseHTTPResponse:

        # TODO добавить поле с количеством сообщенеий для каждого пользователя

        try:
            user_queries.get_user(session=session, user_id=token['id']).is_deleted
        except DBUserDeletedException:
            raise SanicUserDeletedException('User deleted')

        db_user = user_queries.get_users(session)

        response_model = ResponseGetUserDto(db_user, many=True)

        return await self.make_response_json(
            status=200, body=response_model.dump()
        )
