# вспомогательный модуль для создания и чтения токенов

import datetime

import jwt

from jwt.exceptions import PyJWTError

from utils.auth.config import UtilsConfig
from utils.auth.exceptions import ReadTokenException


# функция для генерации токена
def create_token(payload: dict) -> str:
    # ключ будет действителен 1 час
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    return jwt.encode(payload, UtilsConfig.secret_token, algorithm='HS256')


def read_token(token: str) -> dict:
    try:
        return jwt.decode(token, UtilsConfig.secret_token, algorithms='HS256')
    except PyJWTError:
        raise ReadTokenException
