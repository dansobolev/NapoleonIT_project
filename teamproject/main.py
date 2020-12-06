# __name__ - переменная с именем существующего модуля (название файла)
# при запуске файла ему дается имя __main__
# print(__name__) // will print __main__, if we execute exactly this file

from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, json

app = Sanic(__name__)


@app.route('/', methods=['GET', 'POST'])
async def health_endpoint(request: Request) -> HTTPResponse:
    response = {
        'hello': 'world'
    }
    if request.method == 'POST':
        response.update(request.json)

    return json(body=response, status=200)

app.run(
    host='localhost',
    port=8000,
)


