"""
url the router for all handlers.
"""
import os
from pathlib import Path
import inspect
import importlib
from tornado.web import RequestHandler

def get_module_names(s):
    root = Path(__file__).parent.parent
    tmp = s.split('.')
    api_path = root.joinpath(*tmp)
    files = os.listdir(api_path)
    rtn = []
    for file in files:
        if not file.startswith('_') and file.endswith('.py'):
            name = file[:-3]
            rtn.append((f'{s}.{name}', name, tmp[0]))
    return rtn
        
    
def get_urls(modules=[], options={}):
    handler_names = []
    rtn = []
    logger = options.pop('logger')
    for mod, prefix in modules:
        values = get_module_names(mod)
        for m_name, name,  pkg in values:
            module = importlib.import_module(m_name, pkg)
            for attr in dir(module):
                obj = getattr(module, attr)
                if inspect.isclass(obj) and issubclass(obj, RequestHandler) and name not in handler_names:
                        try:
                            urls = getattr(obj, 'urls')
                            for url in urls:
                                if url.startswith('/'):
                                    url = url[1:]
                                url = f'/{prefix}/{name}/{url}'
                                logger.info(f'>>> url: {url:<60} module: {name:<40} ')
                                rtn.append((url, obj, options))
                        except AttributeError:
                            pass
    return rtn
    
if __name__ == '__main__':
    res = get_urls()
    print(res)