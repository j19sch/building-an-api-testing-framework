import falcon
from falcon import testing
import pytest

from api_app.src.app import app


@pytest.fixture
def client():
    return testing.TestClient(app)


def test_knockknock(client):
    response = client.simulate_get('/knockknock')

    assert response.status == falcon.HTTP_OK
    assert response.text == "Who's there?"
