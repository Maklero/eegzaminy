from functools import wraps
from flask import jsonify, request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            token = request.headers['token']
            if token is '':
                return jsonify({'message': 'Token is invalid'}), 403
        except KeyError:
            return jsonify({'message': 'Token is missing!'}), 403

        return f(*args, **kwargs)

    return decorated
