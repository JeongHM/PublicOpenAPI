import json
from datetime import datetime
from flask import Blueprint, request, Response
dust_blueprint = Blueprint('dust', __name__)

from backend.app import db
from backend.common.constants import CONSTANTS_OBJECT
from backend.services.dust_service import DustService
from backend.models.dust_model import DustInfos


def response_format_decorator(func):
    def wrapper(*args, **kwargs):
        res, result = func(*args, **kwargs)
        res['result'] = result
        return Response(json.dumps(res), content_type='application/json; charset=utf-8')
    return wrapper


@dust_blueprint.route('/', methods=['GET'])
def dust_index():
    return 'hello dust index page'

@dust_blueprint.route('/update', methods=['GET'], endpoint='update_dust_infos')
@response_format_decorator
def update_dust_infos():
    headers = request.headers
    if not headers.get('update-key') or headers.get('update-key') != '123':
        return_val = {'data': 'abort page'}
        return CONSTANTS_OBJECT['404'], return_val

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

    for item in rows:
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
    return_val = {'data': 'success'}
    return CONSTANTS_OBJECT['STATUS_CODE']['200'], return_val





@dust_blueprint.route('/current', methods=['GET'], endpoint='get_current_dust_infos')
@response_format_decorator
def get_current_dust_infos():
    headers = request.headers

    dust_service = DustService(headers=headers, bodies=None)
    # if not dust_service.check_headers():
    #     return_val = {'data': 'header info is not validate'}
    #     return CONSTANTS_OBJECT['STATUS_CODE']['404'], return_val
    #
    # if not dust_service.check_bodies():
    #     return_val = {'data': 'param info is not validate'}
    #     return CONSTANTS_OBJECT['STATUS_CODE']['404'], return_val

    date_time = datetime.now().strftime('%Y-%m-%d %H:00')
    # date_time = body.get('date_time')
    # date_time = '2020-02-23 23:00'

    rows = DustInfos.query.filter_by(date_time=date_time).all()
    result = [row.serialize for row in rows]
    if not result:
        return_val = {'data': '데이터가 존재하지 않습니다'}
        return CONSTANTS_OBJECT['STATUS_CODE']['404'], return_val
    return_val = {'data': result}
    return CONSTANTS_OBJECT['STATUS_CODE']['200'], return_val



