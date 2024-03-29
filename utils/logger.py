import logging
from logging.handlers import TimedRotatingFileHandler
import os
from pathlib import Path

from utils.get_env import look_up


def get_logger(name, log_dir=None):
    if log_dir is None:
        log_dir = look_up('LOG_DIR_PATH')
    log_path = Path(log_dir)
    if not log_path.exists():
        print(f'日志路径: {log_path}不存在，创建路径。')
        os.makedirs(log_path)
    log_level = look_up('log_level')
    log_level = log_level or logging.INFO
    log = logging.getLogger(name)
    log.setLevel(log_level)
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    log_file_handler = TimedRotatingFileHandler(
        filename=f'{log_dir}/{name}.log',
        when='w6',
        backupCount=7,
    )
    log_file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    log.addHandler(log_file_handler)
    log.addHandler(console_handler)
    return log
