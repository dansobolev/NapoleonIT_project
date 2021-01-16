# модуль для запросов касательно пользователя

from api.request import RequestCreateUserDto
from db.database import DBSession
from db.exceptions import DBUserAlreadyExistsException, DBUserNotFoundException
from db.models import DBUser


# создание модели пользователя в базе данных
def create_user(session: DBSession, user: RequestCreateUserDto, hashed_password: bytes) -> DBUser:
    # создание модели DBUser
    new_user = DBUser(
        login=user.login,
        password=hashed_password,  # записываем в базу хэшированный пароль
        first_name=user.first_name,
        last_name=user.last_name,
    )

    # сначала попробуем получить пользователя по login перед созданием записи в БД
    # если не None, то получается, что пользователь с таким логином уже есть в БД -> рейзим исключение
    if session.get_user_by_login(new_user.login) is not None:
        raise DBUserAlreadyExistsException

    # добавляем модель в базу данных
    session.add_model(new_user)

    return new_user


# получение пользователя
def get_user(session: DBSession, login: str = None, user_id: int = None) -> DBUser:
    db_user = None

    if login is not None:
        db_user = session.get_user_by_login(login)
    elif user_id is not None:
        db_user = session.get_user_by_id(user_id)

    if db_user is None:
        raise DBUserNotFoundException
    return db_user
