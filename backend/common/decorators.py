import json
from flask import Response


def response_format_decorator(func):
    def wrapper(*args, **kwargs):
        res, result = func(*args, **kwargs)
        res['result'] = result
        res = json.dumps(res, ensure_ascii=False).encode(encoding='utf-8')
        return Response(res, content_type='application/json; charset:utf-8')
    return wrapper
