from sanic.request import Request
from sanic.response import HTTPResponse, json


# аннотация нужно указывать, чтобы IDE знал объекта какого класса
# мы собираемся использовать и каждый раз предлагал нам
# список доступных методов
# также аннотации используют для лучшей читаемости кода
async def health_endpoint(request: Request) -> HTTPResponse:
    response = {
        'hello': 'world'
    }

    if request.method == 'POST':
        response.update(request.json)

    return json(body=response, status=200)
