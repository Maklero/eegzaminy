from flask import Flask
from functions import token_required

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

def test():
    return 'taki tam test'


@app.route('/protected')
@token_required
def test():
    return 'This route is protected by token'


if __name__ == '__main__':
    app.run()
