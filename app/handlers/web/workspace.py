
from pathlib import Path

from tornado.ioloop import IOLoop
from openpyxl import load_workbook

from .base import Base
from ...settings import get_env
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
    async def get(self):
        # print(self.get_argument('q'))
        data = await self.find()
        self.json(data)

    async def post(self):
        res = await self.collection.insert_one(self.json_args)
        self.json({"code": 0, "_id": str(res.inserted_id)})
  
    async def delete(self):
        delete_id = self.json_args.get('del_ids')
        if delete_id is not None:
            if isinstance(delete_id, list):
                many = self.many_ids(delete_id)
                result = await self.collection.bulk_write(many)
                
            else:
                result = await self.collection.delete_one(self.object_id(delete_id))
            count = result.deleted_count
            self.json({'code': 0, 'deleted_count': count})
        else:
            self.json({'code': -1, 'deleted_count': -1})

    async def patch(self):
        res = await self.collection.update_one(self.json_args)
        self.json({'code': 0, 'matched_count': res.matched_count})

def get_sheet_names(file_name):
    wb = load_workbook(file_name)
    res = {}
    for i, name in enumerate(wb.sheetnames):
        res[f'{i}'] = name
    return res

class Upload(Base):
    def post(self):
        excel = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        rtn = {}
        for file in self.request.files['file']:
            if file['content_type'] == excel:
                pth = get_env('data_file_save_path')
                print(pth)
                if not pth:
                    pth = '.'
                path = Path(pth).joinpath('财务报表')
                if not path.exists():
                    path.mkdir()
                file_name = path.joinpath(file['filename'])
                with file_name.open('wb') as f:
                    f.write(file['body'])
                sheet_names = get_sheet_names(file_name)
                rtn[file['filename']] = sheet_names
            else:
                continue
        self.json(rtn)