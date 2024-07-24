import pytest

import requests

from unittest.mock import MagicMock

@pytest.fixture
def mock_response_success():

    mock = MagicMock(spec=requests.Response)

    mock.status_code = 200

    mock.json.return_value = {"message" : "Success"}
    return mock

@pytest.fixture
def mock_response_failed():

    mock = MagicMock(spec=requests.Response)

    mock.status_code = 400

    mock.json.return_value = {"message" : "Failed"}
    return mock


def test_api_call_success_with_mock(mock_response_success):
    response = mock_response_success

    assert response.status_code == 200
    assert response.json() == {"message" : "Success"}
    assert response.status_code != 400

def test_api_call_failed_with_mock(mock_response_failed):
    response = mock_response_failed

    assert response.status_code != 200
    assert response.json() != {"message" : "Success"}
    assert response.status_code == 400
    assert response.json() == {"message" : "Failed"}