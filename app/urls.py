"""
url the router for all handlers.
"""
from app.handlers.wx import WxHandler

urls = [
            (r"/apiwx/wx", WxHandler),
        ]
