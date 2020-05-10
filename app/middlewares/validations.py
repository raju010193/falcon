import ast
import json

class DataValidation(object):
    def process_request(self, req, res):
        data = {}
        try:
            for key in req.params:
                data.update({key: req.get_param(key)})
            req._params = {}
            postData = str(req.stream.read())
            if len(postData) != 0 and req.accept:
                # res_dict = postData.decode('utf-8')
                # print(type(res_dict))
                data.update(ast.literal_eval(postData).decode('utf-8'))
        except SyntaxError as s:
            print('SyntaxError Exception {0}'.format(str(s)))
        except Exception as e:
            print('Exception occurred {0}'.format(str(e)))

from app.db.dbManager import *


class DatabaseCursor(object):

    def __init__(self, config):
        self.config = config
        self.db = DBInterface(config=config)

    def process_resource(self, req, resp, resource):
        if resource is not None:
            if self.db.closed:
                self.db = DBInterface(self.config)
            resource.db = self.db
            resource.cursor = self.db.cursor()

    def process_response(self, req, resp, resource):
        if hasattr(resource, 'cursor'):
            resource.cursor.close()
