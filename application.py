import os
import logging

from flask import Flask
from utils.constants import RESPONSE_CODE
from utils.decorators import formatting_response


def create_app():
    app = Flask(import_name="Test")

    app.secret_key = os.urandom(16)

    from controllers.dust import dust_blueprint
    app.register_blueprint(blueprint=dust_blueprint, url_prefix="/dust")

    return app


application = create_app()


@application.route(rule="/", methods=["GET"], endpoint="health_check")
@formatting_response
def health_check():
    return RESPONSE_CODE["SUCCESS"], None, 200


if __name__ == '__main__':
    application.run(host="localhost", port="5000", debug=False)