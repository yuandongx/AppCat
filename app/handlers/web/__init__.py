from .workspace import Financial, Upload
__all__ = ['urls']
urls = {
    "workspace": {
        "financial": Financial,
        "upload": Upload
    }
}
