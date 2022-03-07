
from tornado.web import RequestHandler
from ...settings import get_setting


class BaseHandler(RequestHandler):

    def initialize(self, **kwarg):
        if db:=get_setting(self.settings, "db"):
            setattr(self, "db", db)

    def prepare(self):
        pass
 
    async def insert(self, **kwargs):
        collection = kwargs.get("collection", None)
        data = kwargs.get("data", None)
        if collection and data:
            await self.db[collection].insert_one(data)
        else:
            if collection is None:
                print(collection) 
            if data is None:
                print(data)
    async def insert_many(self, **kwarg):
        collection = kwargs.get("collection", None)
        data = kwargs.get("data", None)
        if collection is None:
            print(collection) 
        if data is None:
            print(data)
        if not isinstance(data, (list, tuple)):
            data = (data, )
        count = await self.db[collection].insert_many(data)
        return count

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass

    async def query_one(self, **kwargs):
        collection = kwargs.get("collection")
        document = await db[collection].find_one({'i': {'$lt': 1}})
        return document

    async def query_many(self, **kwargs):
        collection = kwargs.get("collection")
        data = []
        for document in await cursor.to_list(length=100):
            data.append(document)
        return data