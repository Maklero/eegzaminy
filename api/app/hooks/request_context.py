from flask import Response


def after_request(response: Response) -> Response:
    try:
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'deny'
        response.headers['server'] = 'api.eegzaminy.pl'
    finally:
        return response

