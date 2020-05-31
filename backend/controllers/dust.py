from flask import Blueprint, request

dust_blueprint = Blueprint(name='dust', import_name=__name__)


@dust_blueprint.route('/', methods=['GET'], endpoint='dust_index')
def dust_index():
    return 'Hello World'


@dust_blueprint.route('/<city>', methods=['GET'], endpoint='dust_info')
def dust_info(city):
    date = request.args.get('date')
    return f'{date}, {city}'