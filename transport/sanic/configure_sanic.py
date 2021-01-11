# файла необходим для создания самого application'a

from sanic import Sanic

from transport.sanic.routes import get_routes


def configure_app():

    app = Sanic(__name__)

    for handler, uri, methods in get_routes():
        app.add_route(
            handler=handler,
            uri=uri,
            methods=methods,
        )

    return app
