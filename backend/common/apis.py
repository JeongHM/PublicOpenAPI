import requests
from configparser import ConfigParser
from urllib.parse import urlencode
from os import path

config = ConfigParser()
config.read(path.abspath(path.join(path.dirname(__file__), '../config.ini')))


class OpenAPI(object):
    def __init__(self, host, path, params):
        self._host = host
        self._path = path
        self._params = params
        self._params['serviceKey'] = config['OPEN_API']['SECRET_KEY']

    def __repr__(self):
        return f" API : {self._host + self._path}"

    def get_json_response(self):
        resp = None
        result_code = None
        total_count = None
        body = None

        try:
            req = requests.get(url=f'{self._host}{self._path}?{urlencode(query=self._params, safe="%")}')

            if not req.ok:
                raise ValueError(f'response is not 200 : {req.status_code}')

            if self._params.get('_returnType') or self._params.get('_type'):
                resp = req.json()

            else:
                # xml to dict
                # dict to json
                pass
            if self._params.get('_type'):
                result_code = resp['response']['header']['resultCode']
                total_count = resp['response']['body']['totalCount']
                body = resp['response']['body']['items']['item']

            elif self._params.get('_returnType'):
                result_code = req.status_code
                total_count = resp['totalCount']
                body = resp['list']

        except Exception as e:
            return e

        else:
            return {
                'result_code': result_code,
                'total_count': total_count,
                'body': body
            }
