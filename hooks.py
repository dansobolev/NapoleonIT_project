# модуль, который должен быть выполнен при старте программы
# в данном случае получается подключение к базе данных

from sqlalchemy import create_engine

from context import Context
from db.database import DataBase


def init_db_sqlite(context: Context):
    uri = r'sqlite:///db.sqlite'
    engine = create_engine(
        uri,
        pool_pre_ping=True,  # для переподключения
    )

    database = DataBase(connection=engine)
    database.check_connection()

    context.set('database', database)

