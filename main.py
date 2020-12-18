from configs.config import ApplicationConfig
from transport.sanic.configure_sanic import configure_app

from context import Context


if __name__ == '__main__':
    config = ApplicationConfig()
    context = Context()
    app = configure_app(config, context)

    app.run(
        host=config.sanic.host,
        port=config.sanic.port,
        workers=config.sanic.workers,
        debug=config.sanic.debug,
    )
