from marshmallow import Schema, fields, post_load

from api.base import RequestDto

from helpers.password.hash import generate_hash


class RequestCreateUserDtoSchema(Schema):
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)

    # после проверки валидации заменяем в словаре значение ключа password на его хэш
    @post_load
    def hash_password(self, data: dict, **kwargs) -> dict:
        password = data['password']
        hashed_password = generate_hash(password)
        data['password'] = hashed_password

        return data


# можно добавить также второго родителя, чтобы IDE знал
# какие в нашей схеме существуют поля
class RequestCreateUserDto(RequestDto, RequestCreateUserDtoSchema):
    __schema__ = RequestCreateUserDtoSchema
