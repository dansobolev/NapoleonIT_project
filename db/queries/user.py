# модуль для запросов касательно пользователя

from api.request import RequestCreateUserDto
from db.database import DBSession
from db.exceptions import UserAlreadyExistsException
from db.models import DBUser


def create_user(session: DBSession, user: RequestCreateUserDto) -> DBUser:
    # создание модели DBUser
    new_user = DBUser(
        login=user.login,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    # сначала попробуем получить пользователя по login перед созданием записи в БД
    # если не None, то получается, что пользователь с таким логином уже есть в БД -> рейзим исключение
    if session.get_user_by_login(new_user.login) is not None:
        raise UserAlreadyExistsException

    # добавляем модель в базу данных
    session.add_model(new_user)

    return new_user
