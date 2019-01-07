from functools import wraps
from flask import jsonify

def route(bp, *args, **kwargs):
    """Serializes the return value of view methods to JSON.

    It turns the JSON output into a Response object with the 
    application/json mimetype.

    Args:
        bp: Flask Blueprint object

    Returns:
        Flask Response object.

    """
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc
        return wrapper

    return decorator
