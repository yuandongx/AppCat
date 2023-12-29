"""
Application
"""
from tornado.ioloop import IOLoop
from tornado.web import Application as App
from motor.motor_tornado import MotorClient
from .urls import get_urls
from .settings import load_env, setup_env
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
        mongo_url = self.env.get('mongodb_url') or self.env.get('mongo_url')
        self.db_client = MotorClient(mongo_url)
        self.api_modules = [
            ("api.handlers.web", 'apiv1')
        ]
        self.logger = get_logger('app')

    def setup(self):
        """
        setup
        :return:
        """
        setup_env()
        self.env = load_env()

    def run(self):
        """
        run
        """
        self.setup()
        route = get_urls(self.api_modules, {"db": self.db_client, 'logger': self.logger})
        app = App(route)
        app.listen(self.port)
        IOLoop.current().start()
