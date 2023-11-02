"""
url the router for all handlers.
"""
from app.handlers.wx import WxHandler, QyHandler

urls = [
    (r"/apiwx/wx", WxHandler),
    (r"/apiwx/qy", QyHandler),
    ]
