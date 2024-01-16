"""
Application
"""
from tornado.ioloop import IOLoop
from tornado.web import Application as App
from motor.motor_tornado import MotorClient

from .get_env import look_up
from .urls import get_urls
from .logger import get_logger


class Application:
    """
    Application
    """

    def __init__(self, port=8000):
        """
        __init__
        :param port:
        """
        self.port = port
        self.env = {}
        self.setup()
        mongo_url = look_up('mongo_url')
        self.db_client = MotorClient(mongo_url)
        self.api_modules = [
            ("api.apiv1.web", 'apiv1')
        ]
        self.logger = get_logger('app')

    def setup(self):
        """
        setup
        :return:
        """
        pass

    def run(self):
        """
        run
        """
        self.setup()
        route = get_urls(self.api_modules, {"db": self.db_client, 'logger': self.logger})
        app = App(route)
        app.listen(self.port)
        IOLoop.current().start()
