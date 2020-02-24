from flask import Blueprint
dust_blueprint = Blueprint('dust', __name__, url_prefix='/api/dust')
from backend.models.dust_infos import DustInfos


@dust_blueprint.route('/', methods=['GET'])
def index():
    return 'welcome dust api'


@dust_blueprint.route('/current/', methods=['GET'])
def get_current_dust_info():
    # ORM
    return '123'