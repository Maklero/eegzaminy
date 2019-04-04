from flask import request
from flask_restful import Resource
from functions import token_required
from Exceptions.Requests import *


# test
class Logging(Resource):
    parameters = {}

    def checkData(self, data):
        missing = False

        if 'login' not in data:
            missing = True
            self.parameters['login'] = False

        if 'password' not in data:
            missing = True
            self.parameters['password'] = False

        if missing:
            raise MissingParametersException

    def generateToken(self):
        return 'a to twoj cholerny token'

    def post(self):
        data = request.form.to_dict()
        try:
            self.parameters = {'login': True, 'password': True}
            self.checkData(data)
            token = self.generateToken()
            return {'message': self.parameters, 'connected': True, 'token': token}, 200

        except MissingParametersException:
            return {'message': self.parameters, 'connected': False, 'token': None}, 403
