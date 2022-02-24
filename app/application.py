"""
Application
"""
from motor import motor_tornado
from tornado.ioloop import IOLoop
from tornado.web import Application as App

from .settings import (APP_VAR_PREFIX, APPLICATION_SETTINGS,
                       DB_CONNECTION_INFO,
                       DEFAULT_APP_SETTINGS)
from .urls import urls


def db_url() -> str:
    return f"mongodb://git"

class Application:
    """
    Application
    """

    def __init__(self, port=8888, db_url=""):
        """
        __init__
        :param port:
        """
        self.port = port
        self.db_client = None
        self.db_url = db_url

    def setup(self):
        """
        setup
        :return:
        """
        self.db_client = motor_tornado.MotorClient(self.db_url)

    def run(self):
        """
        run
        """
        self.setup()
        app = App(urls, db=self.db_client, **APPLICATION_SETTINGS)
        for key in DEFAULT_APP_SETTINGS:
            app.settings[f"{APP_VAR_PREFIX}{key}"] = DEFAULT_APP_SETTINGS[key]
        app.listen(self.port)
        IOLoop.current().start()
