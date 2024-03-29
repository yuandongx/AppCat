"""
settings for application
"""
from pathlib import Path

# 根路径
ROOT = Path(__file__).parent

# 日志路径
LOG_DIR_PATH = ROOT.joinpath('log1')

# 自定义APP变量的前缀值
APP_VAR_PREFIX = "app_"

# 默认端口
APP_PORT = 8001

# app api model列表, 只有在这表时的module查会找查对应的url，生成对应的url
API_MODEL_LIST = {
    "api.v1": "api.v1"
}

APPLICATION_SETTINGS = {
    "debug": True,
    "autoreload": True,
}

MONGODB_URL = "mongodb://root:admin$12345@127.0.0.1:27017/"

WX_TOKEN = "weimaomao"

DATA_FILE_SAVE_PATH = "/home/xuyuandong/workspace/daily-work"
