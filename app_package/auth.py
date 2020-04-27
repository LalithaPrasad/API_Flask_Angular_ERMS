import json
from functools import wraps
from flask import request
from app_package.models import Admin

def valid_token(func):
    @wraps(func)
    def inner(*args, **kwargs):
        admin=Admin.query.get(1)
        token=request.headers.get("token")
        if not (admin and admin.token==token and admin.validate_token()):
            return json.dumps({"message":"InvalidToken"})
        else:
            return func(*args, **kwargs)
    return inner
