"""
url the router for all handlers.
"""
from app.handlers.wx import urls
from app.handlers.web import urls
urls = {
    "apiv1": urls,
    "apiwx": urls,
}
def get_router(options={}):
    def render(parent, values):
        rtn = []
        if isinstance(values, dict):
            for key in values:
                url = f"{parent}/{key}"
                res = render(url, values[key])
                rtn.extend(res)
        else:
            rtn.append((parent, values, options))
        return rtn
    rtn = []
    for key, value in urls.items():
        res = render(f"/{key}", value)
        rtn.extend(res)
    return rtn

if __name__ == '__main__':
    res = get_router()
    print(res)