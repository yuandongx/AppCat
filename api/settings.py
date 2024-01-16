"""
settings for application
"""

# 自定义APP变量的前缀值
APP_VAR_PREFIX = "app_"

# app model列表
API_MODEL_LIST = {
    "apiv1": "apiv1.web"
}

APPLICATION_SETTINGS = {
    "debug": True,
    "autoreload": True,
}


DATA_BASE = {
    "mongo_url": "mongodb://root:admin$12345@127.0.0.1:27017/",
    "mongo_db": "test",
}

WX_TOKEN = "weimaomao"

DATA_FILE_SAVE_PATH = "/home/xuyuandong/workspace/daily-work"
