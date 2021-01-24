from sqlalchemy import Column, String, BOOLEAN, LargeBinary

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
        LargeBinary(),
        nullable=False)

    first_name = Column(String(50))
    last_name = Column(String(50))

    is_deleted = Column(
        BOOLEAN(),
        default=False,
    )
