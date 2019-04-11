from flask import request, jsonify
from flask_restful import Resource
from models import *


class Test(Resource):
    def get(self):
        test = BasicExamModel('ee09')
        question = test.oneQuestion(3)
        print(question.question)
        return {'message': 'ok'}
