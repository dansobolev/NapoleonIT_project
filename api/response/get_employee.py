from marshmallow import Schema, fields

from api.base import ResponseDto


class ResponseGetEmployeeDtoSchema(Schema):
    # employee's id
    eid = fields.Int(required=True, allow_none=False)


class ResponseGetEmployeeDto(ResponseDto, ResponseGetEmployeeDtoSchema):
    __schema__ = ResponseGetEmployeeDtoSchema
