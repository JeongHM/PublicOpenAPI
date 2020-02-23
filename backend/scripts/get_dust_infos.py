from backend.common.apis import OpenAPI
from datetime import datetime
from backend.models.dust_infos import db, DustInfos


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
    resp = api.get_json_response()

    result_code = resp.get('result_code')
    total_count = resp.get('total_count')
    items = resp.get('body')

    if result_code != 200 or total_count < 1:
        raise ValueError(f'Not Validate Result Code [{result_code}] or Count [{total_count}]')

    rows = [{
        'date_time': item.get('dataTime'),
        'busan': item.get('busan'),
        'chungbuk': item.get('chungbuk'),
        'chungnam': item.get('chungnam'),
        'daegu': item.get('daegu'),
        'daejeon': item.get('daejeon'),
        'gangwon': item.get('gangwon'),
        'gwangju': item.get('gwangju'),
        'gyeongbuk': item.get('gyeongbuk'),
        'gyeonggi': item.get('gyeonggi'),
        'gyeongnam': item.get('gyeongnam'),
        'incheon': item.get('incheon'),
        'jeju': item.get('jeju'),
        'jeonbuk': item.get('jeonbuk'),
        'jeonnam': item.get('jeonnam'),
        'sejong': item.get('sejong'),
        'seoul': item.get('seoul'),
        'ulsan': item.get('ulsan')
    } for item in items]
    create_dust_info(items=rows)

def create_dust_info(items):
    for item in items:
        date_time = item.get('date_time')
        del item['date_time']

        for city, pm in item.items():
            event = DustInfos(id=item.get('id'),
                              city=city,
                              pm2=None,
                              pm10=pm,
                              date_time=date_time)
            db.session.add(event)
            db.session.commit()


main()