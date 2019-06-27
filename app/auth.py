from functools import wraps

import jwt
from flask import request, abort, current_app, g


def auth_required(func):
    """
    Checking authorization for resource methods.
    This decorator is intended for use with BiFrost JWT-based authentication
    when JWT_PUBLIC_KEY_RSA_BIFROST environmental variable is provided,
    see the docs: https://docs.walhall.io/bifrost
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_app.config.get('JWT_DISABLED', False):
            header = request.headers.get('Authorization')
            if not header:
                abort(401)
            _, token = header.split()
            try:
                decoded = jwt.decode(token, current_app.config.get('JWT_PUBLIC_KEY_RSA_BIFROST'), algorithms='RS256')
            except jwt.DecodeError:
                abort(401, 'Token is not valid.')
            except jwt.ExpiredSignatureError:
                abort(401, 'Token is expired.')
            else:
                g.organization_uuid = decoded.get('organization_uuid')
        return func(*args, **kwargs)
    return wrapper
