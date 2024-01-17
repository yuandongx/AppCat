"""
url the router for all api.
"""
import os
from pathlib import Path
import inspect
import importlib
from tornado.web import RequestHandler


def get_module_names(root, pkg):
    tmp = pkg.split('.')
    api_path = Path(root).joinpath(*tmp)
    files = os.listdir(api_path)
    rtn = []
    for file in files:
        if not file.startswith('_') and file.endswith('.py'):
            name = file[:-3]
            rtn.append(f'{pkg}.{name}')
    return rtn


def get_urls(root, modules=None, options=None):
    if options is None:
        options = {}
    if modules is None:
        modules = {}
    handler_names = []
    rtn = []
    logger = options.pop('logger')
    for name, pkg in modules.items():
        values = get_module_names(root, pkg)
        for mode in values:
            module = importlib.import_module(mode, pkg)
            for attr in dir(module):
                # 只处理可能是首字母是大写的可能是类的对象
                if attr[0] < 'A' or attr[0] > 'Z':
                    continue
                obj = getattr(module, attr)
                if inspect.isclass(obj) and issubclass(obj, RequestHandler) and mode not in handler_names:
                    try:
                        urls = getattr(obj, 'urls')
                        for url in urls:
                            if url.startswith('/'):
                                url = url[1:]
                            pre_name = mode.replace('.', '/')
                            url = f'/{pre_name}/{url}'
                            logger.info(f'>>> url: {url:<60} module: {mode:<40} ')
                            rtn.append((url, obj, options))
                    except AttributeError:
                        pass
    return rtn


if __name__ == '__main__':
    pass
