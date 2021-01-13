import bcrypt

from helpers.password.exceptions import GeneratePasswordHashException, CheckPasswordHashException


def generate_hash(password_: str) -> bytes:
    try:
        # возвращаем хэшированный пароль и генерируем соль
        return bcrypt.hashpw(
            password=password_.encode(),  # аргумент password ожидает получить строку в виде байтов
            salt=bcrypt.gensalt(),
        )
    except (TypeError, ValueError) as error:
        raise GeneratePasswordHashException(str(error))


def check_hash(password_: str, hash_: bytes) -> bool:
    try:
        # проверяем совпадает ли хэш пароля с тем, который у нас в базе
        return bcrypt.checkpw(
            password=password_.encode(),
            hashed_password=hash_,
        )
    except (TypeError, ValueError) as error:
        raise CheckPasswordHashException(str(error))


if __name__ == '__main__':
    password = 'Dantous201'
    password1 = 'qwerty'
    hsh = generate_hash(password)
    hsh1 = generate_hash(password1)

    print(check_hash(password, hsh1))
