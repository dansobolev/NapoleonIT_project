# модуль для подключение к базе данных

from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session


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
