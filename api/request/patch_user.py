# изменение данных о пользователе

from marshmallow import Schema, fields

from api.base import RequestDto


class RequestPatchUserDtoSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()


class RequestPatchUserDto(RequestDto, RequestPatchUserDtoSchema):
    fields: list
    __schema__ = RequestPatchUserDtoSchema

    def __init__(self, *args, **kwargs):
        self.fields = []
        # super вызовет метод __init__ у родительского класса (RequestDto), передав туда *args и **kwargs
        super(RequestPatchUserDto, self).__init__(*args, **kwargs)

    # переопределяем метод set из базового класса RequestDto
    def set(self, key, value):
        self.fields.append(key)
        super(RequestPatchUserDto, self).set(key, value)
