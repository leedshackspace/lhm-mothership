from flask.views import MethodView
from flask import request
from functools import wraps
from json import loads
from responses.errors.bad_requests import BadDataSupplied, NoCardIdSupplied


def decode_json(f):
    @wraps(f)
    def wrapped_f(self, *args, **kwargs):
        data = request.data
        try:
            json_data = loads(data)
            return f(self, json_data, *args, **kwargs)
        except Exception as e:
            return f(self, None, *args, **kwargs)
    return wrapped_f


class EntryView(MethodView):
    @decode_json
    def post(self, data, *args, **kwargs):
        if data is None:
            return BadDataSupplied()
        if hasattr(data, "cardId"):
            return NoCardIdSupplied()

        return "hi"
