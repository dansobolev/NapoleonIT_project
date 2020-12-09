from sanic import Sanic, response
from sanic.log import logger
from sanic.response import json, text

app = Sanic(__name__)

# DO NOT FORGET to add environment variables next time


@app.route('/')
async def main(request):
    # logging when requesting to the / point
    # logger.info("And there is the log: ")

    return json({
        "parsed": True,
        "url": request.url,
        "query_string": request.query_string,
        "args": request.args,
        "query_args": request.query_args,
    })

if __name__ == "__main__":
    app.run(
        access_log=False,  # disable logging
        host='localhost',
        port=8000,
    )
