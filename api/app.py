from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

import classes.exams as exams

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={
    r"/v1/*": {
        "origins": [
            "http://localhost",
            "http://127.0.0.1:*",
            "http://192.168.8.*",
            "http://192.168.8.*:*",
            "https://localhost",
            "https://*.eegzaminy.pl",
            "http://test.eegzaminy.pl/",
            "*",
        ]
    }
})


# Static Welcome route
@app.route('/')
def hello():
    return jsonify({'message': 'Welcome in eegzaminy.pl API!'})


# API routers
api.add_resource(exams.ExamsList, '/v1/exams/list')  # No parameters
api.add_resource(exams.Exam, '/v1/exams/<name>')  # <name> - exam name
api.add_resource(exams.Verification, '/v1/verify')

if __name__ == '__main__':
    app.run()
