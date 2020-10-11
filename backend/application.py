import os
import logging

from flask import Flask
from flask_cors import CORS
from logging.handlers import RotatingFileHandler


def create_app():
    # init Flask
    app = Flask(import_name=os.getenv("APP_NAME"))

    # Set Flask App sercret Key
    app.secret_key = os.urandom(16)

    # Set Database Config
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{}:{}@{}/{}?charset=utf8".format(
        os.getenv("DB_USER"),
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_DATABASE")
    )
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["CORS_HEADERS"] = "Content-Type"

    # Set logging Config
    logger = logging.getLogger(name=os.getenv("APP_NAME"))
    logger.setLevel(level=logging.INFO)
    logger_formatter = logging.Formatter(fmt='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s')
    logger_handler = RotatingFileHandler(filename='./application.log',
                                         mode='a',
                                         maxBytes=1024 * 1024 * 5,
                                         backupCount=5,
                                         encoding='utf-8')
    logger_handler.setFormatter(fmt=logger_formatter)

    # Set CORS on Flask App
    CORS(app)

    # Set BluePrint
    # from .controllers.api.dust_controller import

    with app.app_context():
        from .models import db
        db.init_app(app=app)
        db.create_all()

    return app


application = create_app()


@application.route(rule="/", method=["GET"], endpoint="index")
def index():
    return "Index Page"


if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5050, debug=True)
