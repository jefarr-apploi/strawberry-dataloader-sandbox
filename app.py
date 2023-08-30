from flask import Flask
import logging
import time
from typing import List
import uvicorn
import asyncio

from strawberry.flask.views import AsyncGraphQLView
from strawberry.dataloader import DataLoader
import strawberry

from asgiref.wsgi import WsgiToAsgi

import os

if True:
    import gevent.monkey
    gevent.monkey.patch_all()

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='api.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
async def hello_world():
    app.logger.info('Hello World endpoint was accessed')
    return 'Hello World'

@strawberry.type
class Role:
    id: strawberry.ID

async def load_roles(keys) -> List[Role]:
    app.logger.info(f"load_roles called with keys {keys}")
    return [Role(id=key) for key in keys]

role_loader = DataLoader(load_fn=load_roles, cache=False)

@strawberry.type
class User:
    id: strawberry.ID

    @strawberry.field
    async def role(self, info) -> Role:
        return await role_loader.load(self.id)

async def load_users(keys) -> List[User]:
    app.logger.info(f"load_users called with keys {keys}")
    return [User(id=key) for key in keys]

users_loader = DataLoader(load_fn=load_users, cache=False)

async def get_user_ids(_):
    return [1,2,3]

user_ids_loader = DataLoader(load_fn=get_user_ids, cache=False)

@strawberry.type
class Query:
    @strawberry.field
    async def get_user(self, id: strawberry.ID) -> User:
        return await users_loader.load(id)

    @strawberry.field
    async def users(self) -> List[int]:
        return await user_ids_loader.load(None)

schema = strawberry.Schema(query=Query)

app.add_url_rule(
    "/gql",
    view_func=AsyncGraphQLView.as_view("graphql_view", schema=schema),
)

asgi_app = WsgiToAsgi(app)

