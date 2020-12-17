import os
import logging

from flask import Flask, request, current_app
from utils.constants import RESPONSE_CODE
from utils.decorators import formatting_response
from logging.handlers import RotatingFileHandler


def create_app():
    app = Flask(import_name="Test")

    app.secret_key = os.urandom(16)

    logger = logging.getLogger(name=__name__)
    logger_format = "[%(process)d] [%(asctime)s] [%(filename)s] [%(funcName)s] [%(lineno)d] : %(message)s"
    logger_formatter = logging.Formatter(fmt=logger_format)
    logger.setLevel(level=logging.INFO)

    logger_handler = RotatingFileHandler(filename="./application.log",
                                         mode="a",
                                         maxBytes=1024 * 1024 * 3,
                                         backupCount=2,
                                         encoding="utf-8")
    logger_handler.setFormatter(fmt=logger_formatter)
    logger.addHandler(hdlr=logger_handler)

    app.logger.addHandler(logger_handler)
    app.logger.setLevel(logging.INFO)

    from controllers.dust import dust_blueprint
    app.register_blueprint(blueprint=dust_blueprint, url_prefix="/dust")

    return app


application = create_app()


@application.before_request
def before_request():
    method = request.method
    url = request.url
    params = dict(request.args) if request.args else None
    body = request.json if request.json else None

    current_app.logger.info(f"[{method}] {url} params: {params} body: {body}")


@application.route(rule="/", methods=["GET"], endpoint="health_check")
@formatting_response
def health_check():
    return RESPONSE_CODE["SUCCESS"], None, 200


if __name__ == '__main__':
    application.run(host="localhost", port="5000", debug=False)