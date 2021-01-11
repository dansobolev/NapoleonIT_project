from sanic.request import Request
from sanic.response import HTTPResponse, json


async def health_endpoint(request: Request) -> HTTPResponse:
    response = {
        'name': 'Daniil',
        'age': 20
    }
    return json(body=response, status=200)
