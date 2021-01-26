from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateMessageDto
from api.response import ResponseGetCreatedMessageDto

from db.database import DBSession
from db.exceptions import DBUserNotFoundException, DBIntegrityException, DBDataException
from db.queries import user as user_queries
from db.queries import message as message_queries

from transport.sanic.endpoints import BaseEndpoint


# класс для создания сообщения пользователем
from transport.sanic.exceptions import SanicUserNotFoundException, SanicDBException


class CreateMessage(BaseEndpoint):

    async def method_post(
            self, request: Request, body: dict, session: DBSession, token: dict, *args, **kwargs
    ) -> BaseHTTPResponse:

        # получение DTO объекта
        request_model = RequestCreateMessageDto(body)

        # проверяем, существуют ли два пользователя в БД (sender and recipient)
        try:
            user_queries.get_user(session=session, user_id=request_model.recipient_id)
            user_queries.get_user(session=session, user_id=token['id'])
        except:
            # TODO DBUserNotFoundException
            pass

        # проверка на то, что оба пользователя удалены
        try:
            user_queries.get_user(session=session, user_id=token['id']).is_deleted
        except:  # TODO DBUserDeletedException:
            pass

        # коммитим данные в БД
        try:
            db_message = message_queries.create_message(session, request_model, token)
            session.commit_session()
        except (DBIntegrityException, DBDataException) as error:
            raise SanicDBException(str(error))

        response_model = ResponseGetCreatedMessageDto(db_message)

        return await self.make_response_json(
            body=response_model.dump(),
            status=201,
        )
