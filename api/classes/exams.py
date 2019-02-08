from flask import jsonify, request
from flask_restful import Resource
import functions as fn


# Return list of exams
class ExamsList(Resource):
    def get(self):
        data = fn.getExamsList()
        data = {'list': data}
        return data, 200
