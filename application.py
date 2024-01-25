"""
Application
"""
from pathlib import Path

from tornado.ioloop import IOLoop
from tornado.web import Application as App
from motor.motor_tornado import MotorClient

import settings
from utils.get_env import look_up
from utils.urls import get_urls
from utils.logger import get_logger


class Application:
    """
    Application
    """

    def __init__(self):
        """
        __init__
        """
        self.port = settings.APP_PORT
        self.env = {}
        self.setup()
        mongo_url = look_up('mongodb_url')
        self.db_client = MotorClient(mongo_url)
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
        root = Path(__file__).parent
        route = get_urls(root, settings.API_MODEL_LIST, {"db": self.db_client, 'logger': self.logger})
        app = App(route)
        app.listen(self.port)
        IOLoop.current().start()
