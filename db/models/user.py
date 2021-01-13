from sqlalchemy import Column, String, VARBINARY

from db.models import BaseModel


class DBUser(BaseModel):

    # название для таблица - как она будет называться в базе данных
    __tablename__ = 'users'

    login = Column(
        String(50),
        unique=True,
        nullable=False,
    )

    password = Column(
        VARBINARY(),
        nullable=False,
    )

    first_name = Column(String(50))
    last_name = Column(String(50))
