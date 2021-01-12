# файл для настройки конфигов всего приложения


from transport.sanic.config import SanicConfig


class ApplicationConfig:
    sanic: SanicConfig

    def __init__(self):
        self.sanic = SanicConfig()
