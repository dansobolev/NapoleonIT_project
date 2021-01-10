from marshmallow import Schema, ValidationError, EXCLUDE
from sanic.exceptions import SanicException


# базовый класс для запросов пользователей (Create, Delete, Patch etc.)
from api.exceptions import ApiValidationException, ApiResponseValidationException


class RequestDto:
    __schema__ = Schema

    def __init__(self, data: dict):
        try:
            valid_data = self.__schema__(unknown=EXCLUDE).load(data)
        except ValidationError as error:
            raise ApiValidationException(error.messages)
        else:
            self._import(valid_data)

    def _import(self, data: dict):
        for name, field in data.items():
            self.set(name, field)

    def set(self, key, value):
        setattr(self, key, value)


# универсальный класс для возвращения ответов
class ResponseDto:
    __schema__ = Schema

    # obj является каким-то питоновским объектом (не важно каким)
    def __init__(self, obj: object):
        """properties = {}

        # prop = property
        for prop in dir(obj):
            # выбираем не приватные методы
            if not prop.startswith('_') and not prop.endswith('_'):
                attr = getattr(obj, prop)
                # отсеиваем вызываемые методы
                if not callable(attr):
                    valid_data['prop'] = attr

        """
        properties = {
            prop: value
            for prop in dir(obj)
            if not prop.startswith('_') and not prop.endswith('_')
               and not callable(value := getattr(obj, prop))
        }

        try:
            self._data = self.__schema__(unknown=EXCLUDE).load(properties)
        except ValidationError as error:
            raise ApiResponseValidationException(error.messages)

    def dump(self) -> dict:
        return self._data