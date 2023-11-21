from tornado.web import RequestHandler

class Base(RequestHandler):

    def initialize(self, db=None):
        self.db = db