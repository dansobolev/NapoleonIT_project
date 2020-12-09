from transport.sanic.configure_sanic import configure_app


if __name__ == '__main__':
    app = configure_app()

    app.run(
        host='localhost',
        port=8000,
    )


