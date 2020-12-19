import unittest

from services.external.open_api import OpenAPI


class ExternalOpenAPIServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._dust_host = "http://openapi.airkorea.or.kr"
        self._dust_path = "/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst"
        self._dust_parameters = {
            "numOfRows": 10,
            "pageNo": 1,
            "itemCode": "PM10",
            "dataGubun": "HOUR",
            "searchCondition": "MONTH",
            "_returnType": "json"
        }

    def test_config_file(self):
        open_api = OpenAPI(host=self._dust_host,
                           path=self._dust_path,
                           parameters=self._dust_parameters)

        self.assertEqual(open_api.set_api_key(), True)

    def test_dust_api(self):
        open_api = OpenAPI(host=self._dust_host,
                           path=self._dust_path,
                           parameters=self._dust_parameters)
        resp = open_api.request()
        self.assertEqual(type(resp), dict)

