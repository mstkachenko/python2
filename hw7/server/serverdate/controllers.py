from datetime import datetime
from protocol import make_response

def date_controller(request):
    return make_response(
        request, 200, datetime.now().timestamp()
    )

def get_human_date(request):
    dt = datetime.now()
    string_dt=dt.strftime('%Y-%m-%d %H:%M')
    return make_response(
        request, 200, string_dt
    )