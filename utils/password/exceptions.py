from sanic.exceptions import SanicException


# основной класс с ошибкой
class PasswordHashException(SanicException):
    status_code = 500


class GeneratePasswordHashException(PasswordHashException):
    pass


class CheckPasswordHashException(PasswordHashException):
    pass
