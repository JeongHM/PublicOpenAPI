from os import path
from backend import create_app

app, db = create_app()

@app.route('/', methods=['GET'])
def index():
    return 'index page'


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)