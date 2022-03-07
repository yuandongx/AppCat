from .base import BaseHandler

class Device(BaseHandler):


    def get(self):
        self.write("ok")

    def post(self):
        print(self.request.body)