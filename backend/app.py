import os
from flask import Flask
from flask_cors import CORS

from configparser import ConfigParser


config = ConfigParser()
config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.ini')))


def create_app():
    application = Flask(__name__)
    application.secret_key = os.urandom(24)

    CORS(app=application)

    from backend.controllers.dust import dust_blueprint
    application.register_blueprint(blueprint=dust_blueprint, url_prefix='/dust')

    return application


app = create_app()


@app.route('/', methods=['GET'])
def index():
    return 'index page'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)