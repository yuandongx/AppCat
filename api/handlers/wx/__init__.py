"""wx"""
from .wx import WxHandler
from .qy import QyHandler
__all__ = ['urls']

urls = {
    "wx": WxHandler,
    "qy": QyHandler,
}
