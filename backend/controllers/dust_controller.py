from flask import Blueprint, request, Response
dust_blueprint = Blueprint('dust', __name__)

from backend.common.constants import CONSTANTS_OBJECT
from backend.services.dust_service import DustService
from backend.models.dust_model import DustInfos


def response_format_decorator(func):
    def wrapper(*args, **kwargs):
        res, result = func(*args, **kwargs)
        res['data'] = result
        print(res)
        print(result)
        return Response(response=res, headers='application/json')
    return wrapper


@dust_blueprint.route('/', methods=['GET'])
def dust_index():
    return 'hello dust index page'



@dust_blueprint.route('/current', methods=['GET'])
@response_format_decorator
def get_current_dust_infos():
    headers = request.headers
    body = request.json

    dust_service = DustService(headers=headers, bodies=body)
    # if not dust_service.check_headers():
    #     return_val = {'data': 'header info is not validate'}
    #     return CONSTANTS_OBJECT['STATUS_CODE']['404'], return_val
    #
    # if not dust_service.check_bodies():
    #     return_val = {'data': 'param info is not validate'}
    #     return CONSTANTS_OBJECT['STATUS_CODE']['404'], return_val


    # date_time = body.get('date_time')
    date_time = '2020-02-23 23:00'

    rows = DustInfos.query.filter_by(date_time=date_time).all()
    result = [row.serialize for row in rows]
    print(result)
    return CONSTANTS_OBJECT['STATUS_CODE']['200'], {'result': result}




