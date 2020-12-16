import json

from copy import deepcopy

from flask import Response, request


def formatting_response(func):
    """
    Make fixed API response format
    :param func: function
    :return:
    """
    def wrapper(*args, **kwargs):
        res, result, status = func(*args, **kwargs)

        if result:
            res_copy = deepcopy(res)
            res_copy['result'] = result
            res = res_copy
        resp = json.dumps(obj=res, ensure_ascii=False, default=str).encode(encoding="utf-8")
        return Response(response=resp, content_type="application/json; charset=utf-8", status=status)
    return wrapper


def api_header_required(func):
    """
    Check header param, when call API must be need custom HTTP header param
    API_KEY
    :param func: function
    :return:
    """
    def wrapper(*args, **kwargs):
        header = request.header.get("API_KEY")
        if not header:
            return False
        return func(*args, **kwargs)
    return wrapper
