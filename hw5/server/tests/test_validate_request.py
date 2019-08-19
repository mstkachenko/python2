import pytest
from datetime import datetime
from protocol import validate_request

@pytest.fixture
def initial_action():
    return 'test'

@pytest.fixture
def initial_data():
    return 'Some data'


@pytest.fixture
def initial_full_request(initial_action, initial_data):
    return {
        'action':initial_action,
        'time':datetime.now().timestamp(),
        'data':initial_data
    }

@pytest.fixture
def initial_not_full_request(initial_action, initial_data):
    return {
        'action':initial_action,
        'data':initial_data
    }


# Проверека функции validate_request, при условии,
# что request содержит одновременно 'action' и 'time'
def test_validate_full_request(initial_full_request):
    actual_validate_full_request = validate_request(initial_full_request)
    assert actual_validate_full_request == True
    
# Проверека функции validate_request, при условии, 
# что request не содержит одновременно 'action' и 'time'
    
def test_validate_not_full_request(initial_not_full_request):
    actual_validate_not_full_request = validate_request(initial_not_full_request)
    assert actual_validate_not_full_request == False