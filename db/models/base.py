import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, TIMESTAMP


Base = declarative_base()


class BaseModel(Base):
    # необходимо для того, чтобы эта таблица не создавалась просто так, а создавалась тогда,
    # когда наследуется
    __abstract__ = True

    id = Column(
        Integer,  # тип поля для целых значений
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True,
    )

    created_at = Column(
        TIMESTAMP,  # специальный тип поля для временных дат
        nullable=False,
        default=datetime.datetime.utcnow,
    )

    update_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,  # при обновлении поля обновляет и время
    )

    def __repr__(self):
        return f'{self.__name__}'
