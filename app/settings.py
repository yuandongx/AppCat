"""

settings for application
"""

# APPLICATION_SETTINGS to the tornado.web.Application constructor settings.
from typing import (
    Dict,
    Any
)


APPLICATION_SETTINGS = {

    "debug": True,

    "autoreload": True,

}

# 自定义APP变量的前缀值

APP_VAR_PREFIX = "wx_"

DB_CONNECTION = {

    "host": "106.75.63.248:27017",

    "username": "test",

    "password": "123456",

    "db": "test",

}

DEFAULT_APP_SETTINGS = {

    "DEFAULT_DBASE_NAME": "mongo_test",

}

WX_TOKEN = "weimaomao"



def get_setting(config: Dict, name: str) -> Any:
    try:
        return config[f"{APP_VAR_PREFIX}{name}"]
    except KeyError:
        try:
            return config[name]
        except KeyError:
            return None