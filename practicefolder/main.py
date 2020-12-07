from sanic import Sanic
from sanic.log import logger
from sanic.response import json

app = Sanic(__name__)

# DO NOT FORGET to add environment variables next time


@app.route('/')
async def main(request):
    logger.info("And there is the log: ")
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(
        # disable logging
        access_log=False,
        host='localhost',
        port=8000,
    )