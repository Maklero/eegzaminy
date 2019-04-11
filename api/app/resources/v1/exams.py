import json
from ..base import BaseResource
from ...models import BasicExamModel, BasicExamSchema, ExamsList, ExamsListSchema
from flask import request


NAMES = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}


examsListSchema = ExamsListSchema(many=True)
ExamSchema = BasicExamSchema(many=True)

class ExamList(BaseResource):
    def get(self):
        exams_list_db = ExamsList.query.all()
        exams_list_db = examsListSchema.dump(exams_list_db).data

        exams_list = []

        for e in exams_list_db:
            exams_list.append(e['exam_name'])

        return self.response({'list': exams_list})


class Exam(BaseResource):
    def get(self, name=None):
        data = {}

        exams_list_db = ExamsList.query.all()
        exams_list_db = examsListSchema.dump(exams_list_db).data
        exams_list = []

        for e in exams_list_db:
            exams_list.append(e['exam_name'])

        if name not in exams_list:
            return self.response({'msg': 'Not found exam!', 'code': 404}, 404)

        ExamData = BasicExamModel(name).questions()

        data = {
            'title': name,
            'questions': ExamSchema.dump(ExamData).data,
            'name': NAMES
        }

        return self.response(data)


class Verification(BaseResource):
    def post(self):
        data = request.form.to_dict()
        questions_in_test = data['list'].split(';')
        questions = {}
        percent: float = 0

        for nr in questions_in_test:
            if nr == '':
                continue
            inr = int(nr)
            ExamData = BasicExamModel(data['egz_name']).oneQuestion(nr=inr)
            qObj = ExamSchema.dump(ExamData).data
            questions[inr] = {
                'q': qObj,
                'valid': qObj[0]['answer'],
                'user': None
            }
            if nr in data:
                questions[inr]['user'] = data[nr]
                if questions[inr]['valid'] == data[nr]:
                    percent += 1
        
        percent = (percent / (len(questions_in_test) - 1)) * 100

        out = {
            'userData': data,
            'questions': questions,
            'percent': percent,
            'name': NAMES
        }
        return self.response(out)
