from protocol import make_response

from decorators import logged #, login_requeired

# @login_requeired
@logged('%(name)s-%(response)s')
def echo_controller(request):
    data = request.get('data')
    return make_response(request, 200, data)
