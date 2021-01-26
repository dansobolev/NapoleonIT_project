from sqlalchemy import Column, String, Integer

from db.models import BaseModel


class DBMessage(BaseModel):

    __tablename__ = 'messages'

    message = Column(
        String(100),
    )

    sender_id = Column(
        Integer,
        nullable=False
    )

    recipient_id = Column(
        Integer,
        nullable=False
    )
