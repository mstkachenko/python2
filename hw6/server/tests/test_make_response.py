import pytest
from datetime import datetime
from protocol import make_response

#Исходные фикстуры 
@pytest.fixture
def initial_action():
    return 'test'

@pytest.fixture
def initial_code():
    return 200

@pytest.fixture
def initial_data():
    return 'Some data'

#Ожидаемые фикстуры
# @pytest.fixture
# def expected_action(initial_action):
#     return initial_action

# @pytest.fixture
# def expected_code(initial_code):
#     return initial_code

# @pytest.fixture
# def expected_data(initial_data):
#     return initial_data

@pytest.fixture
def initial_request(initial_action, initial_data):
    return {
        'action':initial_action,
        'time':datetime.now().timestamp(),
        'data':initial_data
    }


# INITIAL_CODE = 200

# INITIAL_DATA = 'Some data'

# INITIAL_REQUEST = {
#     'action':'test',
#     'time':datetime.now().timestamp(),
#     'data':'Some data'
# }

# EXPECTED_CODE = 200

# EXPECTED_DATA='Some data'

# EXPECTED_ACTION = 'test'

# def setup_function(func):
#     pass

# def teardown_function(func):
#     pass


# EXPECTED_RESPONSE = {
#     'action':'test',
#     'data':'Some data',
#     'time':datetime.now().timestamp(),
#     'code':200
# }

def test_action_make_response(initial_request, initial_code, initial_data, initial_action):
    actual_response = make_response(initial_request, initial_code, initial_data)
    assert actual_response.get('action') == initial_action

def test_code_make_response(initial_request, initial_code, initial_data):
    actual_response = make_response(initial_request, initial_code, initial_data)
    assert actual_response.get('code') == initial_code

def test_data_make_response(initial_request, initial_code, initial_data):
    actual_response = make_response(initial_request, initial_code, initial_data)
    assert actual_response.get('data') == initial_data

