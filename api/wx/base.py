"""
base hanadler for `wx`
"""
from typing import Awaitable, Optional
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    """
    base class to define BaseHandler
    """
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass
