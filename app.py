from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'


@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello'
