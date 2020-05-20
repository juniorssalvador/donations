from functools import wraps
from flask import request, abort


def require_apy_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        print(request.headers.get('API_KEY'))
        if request.headers.get('API_KEY') == 'apyk124578':
            return view_function(*args, **kwargs)
        else:
            abort(401)

    return decorated_function
