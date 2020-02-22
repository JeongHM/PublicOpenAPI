import requests


class OpenAPI(object):
    def __init__(self, host, path, params):
        self._host = host
        self._path = path
        self._params = params
        self._params['serviceKey'] = '123'

    def __repr__(self):
        return f" API : {self._host + self._path}"

    def get_response(self):
        pass

    def get_json_response(self):
        resp = None

        try:
            req = requests.get(url=f'{self._host}{self._path}',
                               params=self._params)
            if not req.ok:
                raise ValueError(f'response is not 200 : {req.status_code}')

            if self._params['_returnType'] or self._params['_type']:
                resp = req.json()
            else:
                # xml to dict
                # dict to json
                pass
            result_code = resp['response']['header']['resultCode']
            total_count = resp['response']['body']['totalCount']
            body = resp['response']['body']['items']['item']

        except Exception as e:
            return e

        else:
            return {
                'result_code': result_code,
                'total_count': total_count,
                'body': body
            }



def main():
    host = 'http://openapi.airkorea.or.kr/openapi/services/rest'
    path = '/ArpltnInforInqireSvc/getCtprvnMesureLIst'
    params = {
        'numOfRows': 100,
        'pageNo': 1,
        'itemCode': 'PM10',
        'dataGubun': 'HOUR',
        '_returnType': 'json'
    }
    api = OpenAPI(host=host, path=path, params=params)
    api.get_json_response()

main()