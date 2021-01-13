# модуль для запросов касательно пользователя

from api.request import RequestCreateUserDto
from db.database import DBSession
from db.models import DBUser


def create_user(session: DBSession, user: RequestCreateUserDto) -> DBUser:
    # создание модели DBUser
    new_user = DBUser(
        login=user.login,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    # добавляем модель в базу данных
    session.add_model(new_user)

    return new_user
