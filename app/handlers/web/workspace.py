from tornado.ioloop import IOLoop
from .base import Base

"""
财务视图
"""
def intsert(collection, data):
    async def do_insert():
        document = {"key": "value"}
        result = await collection.insert_one(document)
        print("result %s" % repr(result.inserted_id))
    IOLoop.current().run_sync(do_insert)

class Financial(Base):
    def get(self):
        self.json("ok")

    async def post(self):
        print(self.json_args)
        collection = self.db.test.test
        res = await collection.insert_one(self.json_args)
        print(res)
        self.json('ok')

    def delete(self):
        self.json("ok")

    def patch(self):
        self.json("ok")