from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateUserDtoSchema(Schema):
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)


# можно добавить также второго родителя, чтобы IDE знал
# какие в нашей схеме существуют поля
class RequestCreateUserDto(RequestDto, RequestCreateUserDtoSchema):
    __schema__ = RequestCreateUserDtoSchema
