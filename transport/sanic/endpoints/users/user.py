from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestPatchUserDto
from api.response import ResponseGetUserDto

from db.database import DBSession
from db.exceptions import DBUserNotFoundException, DBIntegrityException, DBDataException
from db.queries import user as user_queries

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserNotFoundException, SanicDBException, SanicAuthException


class UserEndpoint(BaseEndpoint):

    async def method_patch(
            self, request: Request, body: dict, session: DBSession, user_id: int,  *args, **kwargs
    ) -> BaseHTTPResponse:

        # проверяем, что пользователь не удален из базы (is_deleted != 1)
        if user_queries.get_user(session=session, user_id=body['id']).is_deleted:
            raise SanicAuthException('Not authenticated')

        request_model = RequestPatchUserDto(body)

        try:
            user = user_queries.patch_user(session, request_model, user_id)
        except DBUserNotFoundException:
            raise SanicUserNotFoundException('User not found')

        try:
            session.commit_session()
        except (DBIntegrityException, DBDataException) as error:
            raise SanicDBException(str(error))

        response_model = ResponseGetUserDto(user)

        return await self.make_response_json(status=200, body=response_model.dump())

    async def method_delete(
            self, request: Request, body: dict, session: DBSession, user_id: int, *args, **kwargs
    ) -> BaseHTTPResponse:
        
        try:
            user_queries.delete_user(session, user_id)
        except DBUserNotFoundException:
            raise SanicUserNotFoundException('User not found')

        try:
            session.commit_session()
        except (DBIntegrityException, DBDataException) as error:
            raise SanicDBException(str(error))

        return await self.make_response_json(status=204)
