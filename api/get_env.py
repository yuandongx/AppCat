import os
from . import settings


def look_up(name, default=None):
    prefix = getattr(settings, 'APP_VAR_PREFIX', None)
    if prefix is not None:
        name = f'{prefix}{name}'.upper()
    if value := os.environ.get(name):
        return value
    return getattr(settings, name, default)
