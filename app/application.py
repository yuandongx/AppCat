from .urls import urls
import tornado.web


class Application(object):

    def __init__(self, port=8888):
        self.port = port

    def run(self):
        app = tornado.web.Application(urls)
        app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()
