from typing import List

from api.request import RequestCreateMessageDto

from db.database import DBSession
from db.models import DBMessage


def create_message(session: DBSession, message: RequestCreateMessageDto, token: dict) -> DBMessage:
    # создание модели DBMessage
    new_message = DBMessage(
        message=message.message,
        sender_id=token['id'],
        recipient_id=message.recipient_id,
    )

    # добавляем модель в БД
    session.add_model(new_message)

    return new_message


def get_all_messages(session: DBSession, user_id: int) -> List['DBMessage']:
    return session.get_all_messages(user_id)
