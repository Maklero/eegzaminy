from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


# Static Welcome route
@app.route('/')
def hello():
    return jsonify({'message' : 'Welcom in eegzaminy.pl API!'})


# API routers


if __name__ == '__main__':
    app.run()
