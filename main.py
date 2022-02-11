import tornado.ioloop
import tornado.web
import hashlib

def check_signature(param, signature):
    sha1 = hashlib.sha1()
    param.sort()
    for p in param:
        sha1.update(p.encode())
    hashcode = sha1.hexdigest()
    return hashcode == signature


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        signature = self.get_argument("signature", None)
        timestamp = self.get_argument("timestamp", None)
        nonce = self.get_argument("nonce", None)
        echostr = self.get_argument("echostr", None)
        token = "weimaomao" #请按照公众平台官网\基本配置中信息填写
        checked = check_signature([token, timestamp, nonce], signature)
        if checked:
            self.write(echostr)
        else:
            self.write("")

    def post(self):
        pass


def make_app():
    return tornado.web.Application([
        (r"/wx", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
