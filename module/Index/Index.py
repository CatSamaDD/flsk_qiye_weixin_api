from module import json,reqparse, Resource,requests


class Index(Resource):

    def __init__(self):
        self.usage = {
                        "code": 200,
                        "msg": "success",
                        "usage": {
                            "text": {
                                "api": "{domain:port}/api/Wechat/text/",
                                "corpid": "企业ID",
                                "corpsecret": "应用的凭证密钥",
                                "agentid": "应用ID",
                                "text": "推送内容，支持HTML"
                            },
                            "text_card": {
                                "api": "{domain:port}/api/Wechat/text_card/",
                                "corpid": "企业ID",
                                "corpsecret": "应用的凭证密钥",
                                "agentid": "应用ID",
                                "title": "卡片消息标题",
                                "description": "卡片消息详情内容",
                                "url": "点击卡片消息后跳转的连接"
                            }
                        }
                    }
    def get(self):
        return self.usage,201
    def post(self):
        return self.usage,201
