import datetime

from marshmallow import Schema, fields, post_load, pre_load

from api.base import ResponseDto


class ResponseGetUserByLoginDtoSchema(Schema):
    id = fields.Int(required=True)
    login = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    total_message = fields.Int(default=0)

    # оба декораторы нужна, чтобы преобразовывать объект из datetime.datetime в str
    # до и после валидации
    @pre_load
    @post_load
    def deserialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = self.datetime_to_iso(data['created_at'])

        return data

    @staticmethod
    def datetime_to_iso(date):
        if isinstance(date, datetime.datetime):
            return date.isoformat()
        return date


class ResponseGetUserByLoginDto(ResponseDto, ResponseGetUserByLoginDtoSchema):
    __schema__ = ResponseGetUserByLoginDtoSchema
