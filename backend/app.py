from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    return 'welcome public open api server'


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
