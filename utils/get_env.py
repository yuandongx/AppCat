import os
import settings


def look_up(name, default=None):
    prefix = getattr(settings, 'APP_VAR_PREFIX', None)
    if prefix is not None:
        name = f'{prefix}{name}'.upper()

    value = os.environ.get(name) or getattr(settings, name, default)
    print(f'find env: {name}={value}')
    return value
