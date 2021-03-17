from module import json,reqparse, Resource,requests


class Index(Resource):

    def __init__(self):
        self.usage = {
                        "code": 200,
                        "msg": "success",
                        "author": {
                            "name": "HTMAPI",
                            "desc": "由HTMAPI提供的免费API 服务，官方文档：www.htm.fun"
                        }
                    }
    def get(self):
        return self.usage,201
    def post(self):
        return self.usage,201
