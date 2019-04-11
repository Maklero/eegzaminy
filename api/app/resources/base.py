import json
from flask_restful import Resource
from flask import Response


class BaseResource(Resource):
    @classmethod
    def response(cls, data, status_code=200, content_type='application/json', **kwargs):
        return Response(
            json.dumps(
                data,
                separators=(',', ': '),
                indent=4),
            status=status_code,
            content_type=content_type,
            **kwargs)
