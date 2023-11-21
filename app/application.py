"""
Application
"""
from tornado.ioloop import IOLoop
from tornado.web import Application as App
from motor.motor_tornado import MotorClient
from .urls import get_router
from .settings import load_env
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
        self.env = load_env()
        self.db_client = MotorClient(self.env['mongo_url'])

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
        route = get_router({"db": self.db_client})
        app = App(route)
        app.listen(self.port)
        IOLoop.current().start()
