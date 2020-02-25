from flask import Blueprint, request, jsonify
dust_blueprint = Blueprint('dust', __name__, url_prefix='/api/dust')
from backend.models.dust_infos import DustInfos
from datetime import datetime


@dust_blueprint.route('/', methods=['GET'])
def index():
    return 'welcome dust api'


@dust_blueprint.route('/current/', methods=['GET'])
def get_current_dust_info():
    date_time = request.args.get('date_time')
    if date_time:
        pass
    else:
        # date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        date_time = '2020-02-23 23:00'

    rows = DustInfos.query.filter_by(date_time=date_time).all()
    result = [row.serialize for row in rows]
    return jsonify({'data': result})
