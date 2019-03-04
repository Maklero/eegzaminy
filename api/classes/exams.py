from flask import jsonify, request
from flask_restful import Resource
import functions as fn
from Exceptions.Requests import *

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


class Verification(Resource):
    def post(self):
        data = request.form.to_dict()
        try:
            questionsInTest = data['list'].split(';')
            questions = {}
            percent: float = 0
            for nr in questionsInTest:
                if nr == '':
                    continue
                inr = int(nr)
                qObj = fn.getOneQuestion(nr=inr, egz=data['egz_name'])
                questions[inr] = {
                    'q': qObj,
                    # 'valid': qObj['answer'],
                    'user': None
                }
                if nr in data:
                    questions[inr]['user'] = data[nr]
                    if questions[inr]['valid'] == data[nr]:
                        percent += 1

            percent = (percent / (len(questionsInTest) - 1)) * 100

            out = {
                'userData': data,
                'questions': questions,
                'percent': percent,
                'name': namesDict
            }
            return out, 200

        except MissingDataException:
            return {'err': 'No data'}, 400
