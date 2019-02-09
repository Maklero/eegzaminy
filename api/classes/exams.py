from flask import jsonify, request
from flask_restful import Resource
import functions as fn

namesDict = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}


# Return list of exams
class ExamsList(Resource):
    def get(self):
        data = fn.getExamsList()
        data = {'list': data}
        return data, 200


# Return requested exam
class Exam(Resource):
    def get(self, name=None):
        if name == 'favicon.ico':
            return {'message': 'Ni chuja'}, 404

        examList = fn.getExamsList()
        if name in examList and name != 'egzamin':
            data = {
                'title': name,
                'questions': fn.getQuestions(name),
                'name': namesDict
            }
            return data, 200
        else:
            return 'Exam {} not found'.format(name), 404
