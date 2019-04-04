from functools import wraps
from flask import jsonify, request
from connection import mysqlQuery


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = request.headers['token']
            if token is '':
                return {'message': 'Token is invalid'}, 403
        except KeyError:
            return {'message': 'Token is missing!'}, 403

        return f(*args, **kwargs)

    return decorated


def getExamsList():
    res = mysqlQuery("SHOW TABLES LIKE 'exam_%'", dictionary=False)
    data = []
    for row in res:
        exam = row[0]
        exam = exam.replace('exam_', '')
        data.append(exam)
    return data


def getQuestions(name, quantity=40):
    q = "SELECT * FROM exam_{} ORDER BY RAND() LIMIT {}".format(name, quantity)
    res = mysqlQuery(q)
    return res


def getAnswer(nr, egz):
    q = "SELECT * FROM exam_{} WHERE id = {}".format(egz, nr)
    res = mysqlQuery(q)
    return res[0]


def getOneQuestion(nr, egz):
    q = "SELECT * FROM exam_{} WHERE id = {}".format(egz, nr)
    res = mysqlQuery(q)
    return res[0]
