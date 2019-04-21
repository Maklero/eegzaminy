from flask import Flask
from flask_restful import Api


def load_settings(app: Flask, settings_obj: object):
    app.config.from_object(settings_obj)


def load_extensions(app: Flask):
    from .extensions import ma, db, cors

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)


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
    from .resources.v1 import UserLogin, UserLogoutAccess, UserLogoutRefresh, TokenRefresh, ProtectedResource

    api = Api(api_v1)

    api.add_resource(Greeting, '/')

    # Exams
    api.add_resource(Exam, '/exams/<name>')
    api.add_resource(ExamList, '/exams/list')
    api.add_resource(Verification, '/verify')

    # Admin
    api.add_resource(UserLogin, '/account/login')
    api.add_resource(UserLogoutAccess, '/account/logout/access')
    api.add_resource(UserLogoutRefresh, '/account/logout/refresh')
    api.add_resource(TokenRefresh, '/account/token/refresh')
    api.add_resource(ProtectedResource, '/account/protected')


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
