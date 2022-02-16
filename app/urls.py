"""
url the router for all handlers.
"""
from app.handlers.wx.handler import Handler

urls = [
            (r"/wx", Handler),
        ]
