import pytest
from echo.controllers import echo_controller 
from datetime import datetime
from protocol import make_response

@pytest.fixture
def initial_action():
    return 'test'

@pytest.fixture
def initial_data():
    return 'Some data'

@pytest.fixture
def initial_request(initial_action, initial_data):
    return {
        'action':initial_action,
        'data':initial_data,
        
    }

def test_echo_controller(initial_request):
    actual_echo_controller=echo_controller(initial_request) 
    assert actual_echo_controller == make_response(initial_request, 200, 'Some data')




