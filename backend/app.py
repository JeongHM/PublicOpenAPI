from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser

config = ConfigParser()
config.read(path.abspath(path.join(path.dirname(__file__), 'config.ini')))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQL_ALCHEMY']['URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    return 'welcome public open api server'


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)