import falcon
import falcon_multipart
from app.db.models import Product
import json

def get_data(product):
    return {
        'name': product.name,
        'content': product.content
    }
class ProductAPI(object):
    @staticmethod
    def on_post(req, res):
        data = json.loads(req.stream.read())
        if data:
            pro_obj = Product(name=data.get('name'), content=data.get('content'))
            pro_obj.save()
            res.status = falcon.HTTP_201
            output = {
                'message': 'Your Note Has Been Posted!',
                'status': 200,
                'successful': True
            }
            res.body = json.dumps(output)

    @staticmethod
    def on_get(req, res):
        pro_obj = Product.objects()
        products = []
        for obj in pro_obj:
            products.append(get_data(obj))

        output = {
            'products': products
        }
        print(output)
        res.body = json.dumps(output)
        res.status = falcon.HTTP_200
