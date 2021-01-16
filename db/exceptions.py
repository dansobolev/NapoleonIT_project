class DBIntegrityException(Exception):
    pass


class DBDataException(Exception):
    pass


class DBUserAlreadyExistsException(Exception):
    pass


class DBUserNotFoundException(Exception):
    pass
