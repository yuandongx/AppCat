"""
Application
"""
from tornado.ioloop import IOLoop
from tornado.web import Application as App

from .settings import (APP_VAR_PREFIX, APPLICATION_SETTINGS,
                       DB_CONNECTION,
                       DEFAULT_APP_SETTINGS)
from .urls import urls


def db_url() -> str:
    """
    for db url
    """
    return "mongodb://{username}:{password}@{host}/{db}?\
        retryWrites=true&w=majority".format(**DB_CONNECTION)

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
        self.db_client = None
        self.db_url = db_url()

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
        app = App(urls, db=self.db_client, **APPLICATION_SETTINGS)
        for key, value in DEFAULT_APP_SETTINGS.items():
            app.settings[f"{APP_VAR_PREFIX}{key}"] = value
        app.listen(self.port)
        IOLoop.current().start()
