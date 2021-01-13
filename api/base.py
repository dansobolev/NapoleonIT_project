from marshmallow import Schema, EXCLUDE, ValidationError

from api.exceptions import ApiRequestValidationException, ApiResponseValidationException


# создание класс DTO (data transfer object) объекта
class RequestDto:
    __schema__: Schema

    def __init__(self, data: dict):
        try:
            valid_data = self.__schema__(unknown=EXCLUDE).load(data)
        except ValidationError as error:
            raise ApiRequestValidationException(error.messages)
        else:
            self._import(valid_data)

    def _import(self, data: dict):
        for name, field in data.items():
            self.set(name, field)

    def set(self, key, value):
        setattr(self, key, value)


# универсальный класс для превращения данных в DTO объект
class ResponseDto:
    __schema__: Schema

    def __init__(self, obj: object):
        properties = {}

        # проходимся по атрибутам объекта и ищем те атрибуты,
        # которые нам нужны (атрибуты из схемы) - превращаем объект из DTO в словарь,
        # чтобы потом отправить клиенту на frontpage
        for prop in dir(obj):
            # выбираем не приватные методы
            if not prop.startswith('_') and not prop.endswith('_'):
                attr = getattr(obj, prop)
                if not callable(attr):
                    properties[prop] = attr

        try:
            self._data = self.__schema__(unknown=EXCLUDE).load(properties)
        except ValidationError as error:
            raise ApiResponseValidationException(error.messages)

    def dump(self) -> dict:
        return self._data
