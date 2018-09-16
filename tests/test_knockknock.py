import falcon
from falcon import testing
import pytest
import logging
from pprint import pformat

from api_app.app import api
from api_app.data import BOOKS


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_knockknock(client):
    response = client.simulate_get('/knockknock')

    assert response.status == falcon.HTTP_OK
    assert response.text == "Who's there?"
