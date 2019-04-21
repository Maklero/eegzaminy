from ..base import BaseResource
from ...models import BasicExamModel, BasicExamSchema, ExamsList, ExamsListSchema
from flask import request


class UserLogin(BaseResource):
    def post(self):
        return {'message': 'user login'}


class UserLogoutAccess(BaseResource):
    def post(self):
        return {'message': 'user logout'}


class UserLogoutRefresh(BaseResource):
    def post(self):
        return {'message': 'user logout'}


class TokenRefresh(BaseResource):
    def post(self):
        return {'message': 'Token refresh'}


class ProtectedResource(BaseResource):
    def get(self):
        return {'message': 'to je tajne'}
