# редактирование сообщений

from marshmallow import Schema, fields, post_load

from api.base import RequestDto
from api.exceptions import ApiRequestValidationException


class RequestPatchUserLoginDtoSchema(Schema):
    login = fields.Str()

    # проверяем длину логина на валидность
    @post_load
    def check_login_length(self, data: dict, **kwargs):
        if 'login' in data:
            if len(data['login']) < 6:
                raise ApiRequestValidationException('Bad request')
            return data


class RequestPatchUserLoginDto(RequestDto, RequestPatchUserLoginDtoSchema):
    __schema__ = RequestPatchUserLoginDtoSchema
