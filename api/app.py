from flask import Flask, jsonify
from flask_restful import Api

import classes.exams as exams

app = Flask(__name__)
api = Api(app)


# Static Welcome route
@app.route('/')
def hello():
    return jsonify({'message' : 'Welcom in eegzaminy.pl API!'})


# API routers
api.add_resource(exams.ExamsList, '/v1/exams/list')  # No parameters

if __name__ == '__main__':
    app.run()
