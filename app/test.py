from functools import wraps

class A:


    def __init__(self, *args, **kwargs):
        print(args, kwargs)
    
    def __call__(self, fnc):

        @wraps(fnc)
        def wrapper(*arg, **kwargs):
            print(arg, kwargs)
            return fnc(*arg, **kwargs)
        return wrapper

@A("a", "c", d="D")
class B:

    def __init__(self, *args, **kwargs):
        print(args, kwargs)
    
@A("a", "c", d="D")
class C(B):
    pass

if __name__ == "__main__":
    b = B(1, 2, 3, 4)
    c = C(5, 54, 65, d=43, f=43)