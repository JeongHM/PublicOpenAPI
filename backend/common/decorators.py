import json
from flask import Response


def response_format_decorator(func):
    def wrapper(*args, **kwargs):
        res, result = func(*args, **kwargs)
        res['result'] = result
        return Response(json.dumps(res), content_type='application/json; charset=utf-8')
    return wrapper