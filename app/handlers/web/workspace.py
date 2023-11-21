from .base import Base

"""
财务视图
"""
class Financial(Base):
    def get(self):
        self.json("ok")

    def post(self):
        pass

    def delete(self):
        self.json("ok")

    def patch(self):
        self.json("ok")