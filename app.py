from flask import Flask
import logging
import time

import gevent.monkey

gevent.monkey.patch_all()

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
    time.sleep(0.01)
    return 'Hello World'

if __name__ == '__main__':
    app.run()
