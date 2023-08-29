from flask import Flask
import logging
import time
#from hypercorn.config import Config
#from hypercorn.asyncio import serve
import uvicorn
import asyncio

from asgiref.wsgi import WsgiToAsgi

# import gevent.monkey

# gevent.monkey.patch_all()

# import asyncio
# import asyncio_gevent

# I had high hopes for this, but sadly it didn't fix the issue
# asyncio.set_event_loop_policy(asyncio_gevent.EventLoopPolicy())

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='api.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
async def hello_world():
    app.logger.info('Hello World endpoint was accessed')
    time.sleep(0.02)
    return 'Hello World'


asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    # Hypercorn
    # config = Config()
    # config.bind = ["0.0.0.0:8000"]
    # asyncio.run(serve(asgi_app, config))

    # Uvicorn
    # config = uvicorn.Config("app:asgi_app", host="0.0.0.0", port=8000, log_level="info")
    # server = uvicorn.Server(config)
    # server.run()
    pass
