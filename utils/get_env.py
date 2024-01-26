import os
import settings


def look_up(name, default=None):
    prefix = getattr(settings, 'APP_VAR_PREFIX', None)
    if prefix is not None:
        env_name = f'{prefix}{name}'
    else:
        env_name = name
    name = name.upper()
    env_name = env_name.upper()
    value = os.environ.get(env_name) or getattr(settings, name, default)
    print(f'find env: {name}={value}')
    return value
