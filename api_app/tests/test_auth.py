import falcon
from falcon import testing
import pytest

from api_app.src.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_post_auth(client):
    response = client.simulate_post('/token/%s' % 'user01')

    assert response.status == falcon.HTTP_CREATED
    assert 'token' in response.json.keys()
