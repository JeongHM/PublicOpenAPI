from flask import Blueprint, request, jsonify
dust_blueprint = Blueprint('dust', __name__, url_prefix='/api/dust')
from backend.models.dust_infos import DustInfos
from backend.common.decorators import response_format_decorator

@dust_blueprint.route('/', methods=['GET'], endpoint='index')
def index():
    return 'welcome dust api'


@dust_blueprint.route('/update', methods=['GET'], endpoint='update_dust_info')
@response_format_decorator
def update_dust_info():
    headers = dict(request.headers)
    if headers.get('api-key') == "dkssudgktpdy":
        pass
    else:
        result = {'data': '잘못된 접근입니다'}
        return {'code': 404, 'data': None}, result

@dust_blueprint.route('/current/', methods=['GET'], endpoint='get_current_dust_info')
@response_format_decorator
def get_current_dust_info():
    date_time = request.args.get('date_time')
    if date_time:
        pass
    else:
        date_time = '2020-02-23 23:00'

    rows = DustInfos.query.filter_by(date_time=date_time).all()
    result = [row.serialize for row in rows]
    return {'code': 200, 'data': None}, result
