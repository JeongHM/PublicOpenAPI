import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.controllers.dust_controller import dust_blueprint
from configparser import ConfigParser

config = ConfigParser()
config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.ini')))

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(dust_blueprint, url_prefix='/dust')
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQL_ALCHEMY']['URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)


@app.route('/', methods=['GET'])
def index():
    return 'index page'


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)