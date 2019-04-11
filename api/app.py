from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from data.data import data

DB_URI = "mysql+pymysql://{}:{}@{}/{}".format(data['user'], data['passwd'], data['host'], data['database'])

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
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
import classes.exams as exams

api.add_resource(exams.ExamsList, '/v1/exams/list')  # No parameters
api.add_resource(exams.Exam, '/v1/exams/<name>')  # <name> - exam name
api.add_resource(exams.Verification, '/v1/verify')


# Admin routers
import classes.admin as admin

api.add_resource(admin.Logging, '/v1/admin/logging')  # token required

# test router
from test import Test
api.add_resource(Test, '/v1/test')

if __name__ == '__main__':
    app.run()
