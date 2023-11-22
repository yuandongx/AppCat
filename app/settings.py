"""
settings for application
"""
# APPLICATION_SETTINGS to the tornado.web.Application constructor settings.
import os

APPLICATION_SETTINGS = {
    "debug": True,
    "autoreload": True,
}
# 自定义APP变量的前缀值
APP_VAR_PREFIX = "app_"
DB_CONNECTION = {
    "mongo_url": "mongodb://root:admin$12345@127.0.0.1:27017/",
    "mongo_db": "test",
}

WX_TOKEN = "weimaomao"

def load_env():
    config = {"wx_token": "weimaomao"}
    config.update(APPLICATION_SETTINGS)
    config.update(DB_CONNECTION)
    for key, value in os.environ.items():
        key = key.lower()
        if key.startswith(APP_VAR_PREFIX):
            _key = key.replace(APP_VAR_PREFIX, '')
            config[_key] = value
    return config

if __name__ == '__main__':
    cfg = load_env()
    print(cfg)