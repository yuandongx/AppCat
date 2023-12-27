"""
Application
"""
from tornado.ioloop import IOLoop
from tornado.web import Application as App
from motor.motor_tornado import MotorClient
from .urls import get_router
from .settings import load_env, setup_env
class Application:
    """
    Application
    """

    def __init__(self, port=8080):
        """
        __init__
        :param port:
        """
        self.port = port
        self.env = {}
        self.setup()
        mongo_url = self.env.get('mongodb_url') or self.env.get('mongo_url')
        self.db_client = MotorClient(mongo_url)

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
        route = get_router({"db": self.db_client})
        app = App(route)
        app.listen(self.port)
        IOLoop.current().start()
