from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestPatchUserPasswordDto
from api.response import ResponseGetUserDto

from db.database import DBSession
from db.exceptions import DBUserNotFoundException, DBIntegrityException, DBDataException, DBUserDeletedException
from db.queries import user as user_queries

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserNotFoundException, SanicDBException, SanicUserDeletedException, \
    SanicPasswordHashException
from utils.password import generate_hash, GeneratePasswordHashException


class ChangePasswordEndpoint(BaseEndpoint):

    async def method_patch(
            self, request: Request, body: dict, session: DBSession, user_id: int, token: dict, *args, **kwargs
    ) -> BaseHTTPResponse:

        # проверяем, что пользователь посылает запрос от своего имени
        if token.get('id') != user_id:
            return await self.make_response_json(status=403)

        request_model = RequestPatchUserPasswordDto(body)

        try:
            hashed_password = generate_hash(request_model.password)
        except GeneratePasswordHashException as error:
            raise SanicPasswordHashException(str(error))

        try:
            user_queries.change_password(session, hashed_password, user_id)
        except DBUserNotFoundException:
            raise SanicUserNotFoundException('User not found')

        try:
            session.commit_session()
        except (DBIntegrityException, DBDataException) as error:
            raise SanicDBException(str(error))

        return await self.make_response_json(status=200)
