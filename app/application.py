"""
Application
"""
from tornado.ioloop import IOLoop
from tornado.web import Application as App

from .settings import APPLICATION_SETTINGS
from .handlers.views import urls


def make_app(port=8888):
    app = App(urls, **APPLICATION_SETTINGS)
    app.listen(port)
    IOLoop.current().start()