'''
视图基类
'''
from datetime import datetime
import json
from bson.objectid import ObjectId
from tornado.web import RequestHandler
from pymongo import DeleteOne, DeleteMany

def refactor_date(d):
    if isinstance(d, datetime):
        return d.strftime("%Y-%m-%d")
    else:
        return str(d)

def render(data):
    if isinstance(data, (str, int, float, bool)):
        return data
    elif isinstance(data, (list, tuple)):
        return [render(item) for item in data]
    elif isinstance(data, dict):
        return {key: render(value) for key, value in data.items()}
    elif isinstance(data, datetime):
        return refactor_date(data)
    return data

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
            self.write(data)

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            data = json.loads(self.request.body)
            self.json_args = data.get('data') or data
        else:
            self.json_args = None

    @staticmethod
    def object_id(_id):
        return ObjectId(_id)
    
    @staticmethod
    def many_ids(array):
        return [{'_id': ObjectId(item) for item in array}]
    
    def find2(self, filters={}):
        data = []
        course = self.collection.find(filters)
        def callback(result, error):
            if error:
                raise error
            elif result:
                result['_id'] = str(result['_id'])
                print(result)
                data.append(result)
            else:
                print("done")
                
        course.each(callback=callback)
        return data
    
    
    async def find(self, filters={}):
        data = []
        cursor = self.collection.find(filters)
        while await cursor.fetch_next:
            doc = cursor.next_object()
            doc['_id'] = str(doc['_id'])
            data.append(render(doc))
            print("done")
        return data