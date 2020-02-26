
def response_format_decorator(func):
    def wrapper(*args, **kwargs):
        res, result = func(*args, **kwargs)
        res['data'] = result
        return res
    return wrapper
