from datetime import datetime
import json
from tornado.web import RequestHandler


class Base(RequestHandler):

    def initialize(self, db=None):
        self.db = db
        now = datetime.now()
        self.current_year = now.year
        self.current_month = now.month
        self.current_day = now.month
        self.current_weekday = now.weekday
        self.default_collection = f'c_{self.current_year}'

    
    def json(self, data):
        if isinstance(data, dict):
            self.write(data)
        else:
            self.write({'data': data})
        