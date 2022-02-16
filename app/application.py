"""
Application
"""
from tornado.web import Application as App
from tornado.ioloop import IOLoop
from .urls import urls
from .settings import APPLICATION_SETTINGS


class Application:
    """
    Application
    """

    def __init__(self, port=8888):
        """
        __init__
        :param port:
        """
        self.port = port

    def setup(self):
        print("setup")

    def run(self):
        """
        run
        """
        self.setup()
        app = App(urls, **APPLICATION_SETTINGS)
        app.listen(self.port)
        IOLoop.current().start()
