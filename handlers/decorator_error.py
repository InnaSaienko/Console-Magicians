from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        pass
    return inner