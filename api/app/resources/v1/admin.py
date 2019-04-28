from ..base import BaseResource
from ...models import (
    BasicExamModel,
    BasicExamSchema,
    ExamsList,
    ExamsListSchema,
    UserModel
)
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)
from flask import request
from flask_restful import reqparse

# potem do poprawy
parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(BaseResource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}, 409

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password'])
        )
        try:
            new_user.add_user()
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'accessToken': access_token,
                'refreshToken': refresh_token
            }, 201
        except:
            return {'message', 'Something went wrong'}, 500


class UserLogin(BaseResource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return {'message': 'User {} doesn\' exists'.format(data['username'])}, 401

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'accessToken': access_token,
                'refreshToken': refresh_token
            }, 200
        else:
            return {'message': 'Wrong credentials'}, 401


class UserLogoutAccess(BaseResource):
    def post(self):
        return {'message': 'user logout'}


class UserLogoutRefresh(BaseResource):
    def post(self):
        return {'message': 'user logout'}


class TokenRefresh(BaseResource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(current_user)
        return {'accessToken': access_token}


class ProtectedResource(BaseResource):
    @jwt_required
    def get(self):
        return {'message': 'to je tajne'}
