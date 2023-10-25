from typing import Awaitable, Optional
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass