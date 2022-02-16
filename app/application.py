"""
Application
"""
from tornado.web import Application as App
from tornado.ioloop import IOLoop
from .urls import urls
from .settings import APPLICATION_SETTINGS


class Application(object):

    def __init__(self, port=8888):
        self.port = port

    def run(self):
        app = App(urls, **APPLICATION_SETTINGS)
        app.listen(self.port)
        IOLoop.current().start()
