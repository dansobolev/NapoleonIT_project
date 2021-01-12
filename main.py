# файл main.py необходим исключительно для запуска программы

from transport.sanic.configure_sanic import configure_app
from configs.config import ApplicationConfig


if __name__ == '__main__':
    config = ApplicationConfig()
    app = configure_app(config)

    app.run(
        host=config.sanic.host,
        port=config.sanic.port,
        workers=config.sanic.workers,
        debug=config.sanic.debug,
    )
