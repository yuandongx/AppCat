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

DEFAULT_ENV = {
    'data_file_save_path': "/home/xuyuandong/workspace/daily-work",
}

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

def setup_env(**cfg):
    DEFAULT_ENV.update(cfg)
    for k, v in DEFAULT_ENV.items():
        if not k.startswith(APP_VAR_PREFIX):
            key = f'{APP_VAR_PREFIX}{k}'
        key = key.upper()
        os.environ[key] = v

def get_env(name):
    if not name.startswith(APP_VAR_PREFIX):
        name = f'{APP_VAR_PREFIX}{name}'
    name = name.upper()
    try:
        return os.environ[name]
    except:
        return None

if __name__ == '__main__':
    cfg = load_env()
    print(cfg)