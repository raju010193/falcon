import falcon
from falcon_multipart.middleware import MultipartMiddleware

from app.middlewares import validations as _middleware
from app.db.dbManager import DBInterface
from routes import routes as _routes

config = {
    'host': '127.0.0.1',
    'name': 'product',
    'port': 27017

}
d = DBInterface(config=config)
middlewares = [MultipartMiddleware()]

api = falcon.API(middleware=middlewares)

for api_route, api_class in _routes.items():
    api.add_route(api_route, api_class)
