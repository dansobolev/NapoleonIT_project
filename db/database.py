# модуль для подключения к базе данных

from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import sessionmaker, Session

from db.models import BaseModel, DBUser

from db.exceptions import DBIntegrityException, DBDataException


# класс для реализации функционала сессии
class DBSession:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    # выполнение запросов
    def query(self, *args, **kwargs):
        return self._session.query(*args, **kwargs)

    # закрытие сессии
    def close_session(self):
        self._session.close()

    # добавления модели в базу данных
    def add_model(self, model: BaseModel):
        try:
            # экземпляр класса Session имеет встроенный метод add
            # для добавления объекта в базу данных
            self._session.add(model)
        except IntegrityError as error:
            raise DBIntegrityException(error)
        except DataError as error:
            raise DBDataException(error)

    # поиск пользователя по login
    def get_user_by_login(self, login: str) -> DBUser:
        return self._session.query(DBUser).filter(DBUser.login == login).first()

    # фиксирование сессии
    def commit_session(self, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as error:
            raise DBIntegrityException(error)
        except DataError as error:
            raise DBDataException(error)

        if need_close:
            self.close_session()


class DataBase:
    connection: Engine
    session_factory: sessionmaker

    _test_query = 'SELECT 1'

    def __init__(self, connection: Engine):
        self.connection = connection
        self.session_factory = sessionmaker(bind=self.connection)

    # проверка соединения
    def check_connection(self):
        self.connection.execute(self._test_query).fetchone()

    # создание сессии
    def make_session(self) -> DBSession:
        session = self.session_factory()
        return DBSession(session)
