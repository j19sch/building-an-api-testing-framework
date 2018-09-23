import falcon
from falcon import testing
import pytest

from api_app.src.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_knockknock(client):
    response = client.simulate_get('/knockknock')

    assert response.status == falcon.HTTP_OK
    assert response.text == "Who's there?"
