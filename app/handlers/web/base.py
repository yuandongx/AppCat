'''
视图基类
'''
from datetime import datetime
import json
from tornado.web import RequestHandler


class Base(RequestHandler):
    '''
    定义集合的名称
    定义数据库的名称
    '''
    default_col_name = None
    default_db_name = None

    def initialize(self, db=None):
        '''初始化设置'''
        now = datetime.now() # 当前年月
        self.current_year = now.year
        self.current_month = now.month
        self.current_day = now.month
        self.current_weekday = now.weekday
        
        # 数据库相关的初始化
        self.default_col_name = self.default_col_name or f'c_{self.current_year}'
        self.default_db_name = self.default_db_name or f'db_{self.current_year}'
        self.db = db[self.default_db_name]
        self.collection = self.db[self.default_col_name]

    def json(self, data):
        if isinstance(data, dict):
            self.write(data)
        else:
            self.write({'data': data})

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None
