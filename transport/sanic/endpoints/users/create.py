from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateUserDto

from db.database import DBSession
from db.queries import user as user_queries
from db.exceptions import DBIntegrityException, DBDataException, UserAlreadyExistsException

from transport.sanic.endpoints import BaseEndpoint

from utils.password import generate_hash


# Endpoint для обработки запроса на создание пользователя
class CreateUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session: DBSession, *args, **kwargs) -> BaseHTTPResponse:

        # DTO объект
        request_model = RequestCreateUserDto(body)

        hashed_password = generate_hash(request_model.password)

        try:
            # экземпляр базы данных
            user_queries.create_user(session, request_model, hashed_password)
            session.commit_session()
        # ошибка уникальность, то есть подразумевается, что такой пользователь
        # уже существует в базе
        except UserAlreadyExistsException:
            return await self.make_response_json(status=409, message='User already exists')
        except (DBIntegrityException, DBDataException) as error:
            return await self.make_response_json(status=500, message=str(error))

        return await self.make_response_json(status=201)
