from flask import Blueprint

from utils.constants import RESPONSE_CODE

dust_blueprint = Blueprint(name="dust", import_name=__name__)


@dust_blueprint.route(rule="/", methods=["GET"], endpoint="get_dust_info")
def get_dust_info():
    return RESPONSE_CODE["SUCCESS"], 200
