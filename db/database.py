from sqlite3 import IntegrityError, DataError
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from db.exceptions import DBIntegrityException, DBDataException
from db.models import BaseModel


class DBSession:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def query(self, *args, **kwargs):
        return self._session.query(*args, **kwargs)

    def close_session(self):
        self._session.close()

    def add_model(self, model: BaseModel):
        try:
            # встроенный метод .add
            self._session.add(model)
        except IntegrityError as error:
            raise DBIntegrityException(error)
        except DataError as error:
            raise DBDataException(error)

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

    def check_connection(self):
        self.connection.execute(self._test_query).fetchone()

    def make_session(self) -> DBSession:
        session = self.session_factory()
        return DBSession(session)

