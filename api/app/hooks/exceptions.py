import json
from flask import Response
from werkzeug.exceptions import HTTPException


def http_exception_handler(e: HTTPException) -> Response:
    return Response(json.dumps({'msg': e.description, 'code': e.code}, separators=(',', ': '), indent=4), e.code, content_type='application/json')


def broad_exception_handler(e: Exception) -> Response:
    # TODO: Automatically send notification by email or SMS to notify the administrator of a critical error.

    return Response(json.dumps({'msg': str(e), 'code': 500}, separators=(',', ': '), indent=4), 500, content_type='application/json')

