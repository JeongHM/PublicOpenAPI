from backend.services.externals.open_api import OpenAPI


class DustInternalSerivce(object):
    def __init__(self, city=None, date=None):
        self._city = city
        self._date = date
        self._host = 'http://openapi.airkorea.or.kr/openapi/services/rest'
        self._path = '/ArpltnInforInqireSvc/getCtprvnMesureLIst'
        self._params = None

        # params = {
        #     'numOfRows': 100,
        #     'pageNo': 1,
        #     'itemCode': 'PM10',
        #     'dataGubun': 'HOUR',
        #     '_returnType': 'json'
        # }

    # def validate_params(self):
    #     if

    def get_dust_info_by_city(self):
        pass
    
    def get_dust_detail_info_by_city(self):
        pass

    def get_dust_info_by_date(self):
        pass

