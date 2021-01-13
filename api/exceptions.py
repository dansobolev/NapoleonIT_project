from sanic.exceptions import SanicException


class ValidationException(SanicException):
    status_code = 400


class ApiRequestValidationException(ValidationException):
    pass


class ApiResponseValidationException(ValidationException):
    status_code = 500
