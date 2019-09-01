import logging  
from functools import wraps
from protocol import make_response


logger = logging.getLogger('server decorators')

def logged(log_format):
    def decorator(func):
        @wraps(func)
        def wrapper (request):
            response = func(request)
            logger.debug(log_format % {'name': func.__name__, 'request':request, 'response': response})
            return response
        return wrapper
    return decorator

def login_requeired(func):
    @wraps(func)
    def wrapper(request):
        if 'token' in request and request.get('token'):
            return func(request)
        return make_response(request, 401, 'Autentication requeried')
    return wrapper