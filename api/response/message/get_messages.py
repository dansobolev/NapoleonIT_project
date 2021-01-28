import datetime

from marshmallow import Schema, fields, pre_load, post_load

from api.base import ResponseDto


class ResponseGetMessageDtoSchema(Schema):
    id = fields.Int(required=True)
    sender_id = fields.Int(required=True)
    recipient_id = fields.Int(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
    message = fields.Str(required=True, allow_none=False)

    # TODO добавить поле is_read и выводить его

    # оба декораторы нужна, чтобы преобразовывать объект из datetime.datetime в str
    # до и после валидации
    @pre_load
    @post_load
    def deserialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = self.datetime_to_iso(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = self.datetime_to_iso(data['updated_at'])

        return data

    @staticmethod
    def datetime_to_iso(date):
        if isinstance(date, datetime.datetime):
            return date.isoformat()
        return date


class ResponseGetMessageDto(ResponseDto, ResponseGetMessageDtoSchema):
    __schema__ = ResponseGetMessageDtoSchema
