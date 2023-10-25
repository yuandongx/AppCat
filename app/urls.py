"""
url the router for all handlers.
"""
from app.handlers.wx import WxHandler

urls = [
            (r"/wx", WxHandler),
        ]
