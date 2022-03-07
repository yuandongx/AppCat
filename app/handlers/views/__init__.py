"""wx"""
from .base import BaseHandler
from .device import Device

urls = [
    ("/apiV1/test", BaseHandler),
    ("/apiV1/test2", Device),
]

__all__ = ["urls"]