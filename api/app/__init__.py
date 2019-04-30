import random
from flask import Flask
from flask_restful import Api


def load_settings(app: Flask, settings_obj: object):
    app.config.from_object(settings_obj)


def load_extensions(app: Flask):
    from .extensions import ma, db, cors, jwt

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)


def load_hooks(app: Flask):
    from .hooks.request_context import after_request
    from .hooks.exceptions import http_exception_handler, broad_exception_handler
    from werkzeug.exceptions import HTTPException

    app.after_request(after_request)

    app.register_error_handler(HTTPException, http_exception_handler)
    app.register_error_handler(Exception, broad_exception_handler)


def load_resources():
    # API v1
    from .resources.v1 import api_v1
    from .resources.v1 import Greeting, Exam, ExamList, Verification
    from .resources.v1 import UserLogin, UserLogoutAccess, UserLogoutRefresh, TokenRefresh, ProtectedResource, UserRegistration

    api = Api(api_v1)

    def fix_error():
        endpoint = str(random.randint(1, 99999999999999999))
        return endpoint

    api.add_resource(Greeting, '/', endpoint=fix_error())

    # Exams
    api.add_resource(Exam, '/exams/<name>', endpoint=fix_error())
    api.add_resource(ExamList, '/exams/list', endpoint=fix_error())
    api.add_resource(Verification, '/verify', endpoint=fix_error())

    # Admin
    api.add_resource(UserRegistration, '/account/registration', endpoint=fix_error())
    api.add_resource(UserLogin, '/account/login', endpoint=fix_error())
    api.add_resource(UserLogoutAccess, '/account/logout/access', endpoint=fix_error())
    api.add_resource(UserLogoutRefresh, '/account/logout/refresh', endpoint=fix_error())
    api.add_resource(TokenRefresh, '/account/token/refresh', endpoint=fix_error())
    api.add_resource(ProtectedResource, '/account/protected', endpoint=fix_error())


def register_blueprints(app: Flask):
    from .resources.v1 import api_v1

    app.register_blueprint(api_v1, url_prefix='/v1')


def create_app(settings_obj: object) -> Flask:
    app = Flask('EegzaminyAPI')

    load_settings(app, settings_obj)
    load_extensions(app)
    load_hooks(app)
    load_resources()

    register_blueprints(app)

    return app
