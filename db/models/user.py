from sqlalchemy import Column, String

from db.models import BaseModel


class DBUser(BaseModel):

    # названия для таблица - как она будет называться в базе данных
    __tablename__ = 'users'

    login = Column(String(50))
    password = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))
