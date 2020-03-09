from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser

def create_app():
    app = Flask(__name__)

    config = ConfigParser()
    config.read(path.abspath(path.join(path.dirname(__file__), 'config.ini')))

    app.config['SQLALCHEMY_DATABASE_URI'] = config['SQL_ALCHEMY']['URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    with app.app_context():
        from backend.controllers.api.dust import dust_blueprint
        app.register_blueprint(dust_blueprint)

        return app, db