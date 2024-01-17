"""
settings for application
"""

# 自定义APP变量的前缀值
APP_VAR_PREFIX = "app_"

# app api model列表, 只有在这表时的module查会找查对应的url，生成对应的url
API_MODEL_LIST = {
    "api.v1": "api.v1"
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