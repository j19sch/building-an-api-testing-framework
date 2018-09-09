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


def test_get_books(client):
    expected = BOOKS

    response = client.simulate_get('/books')

    logging.info("%s: %s" % (response.status, pformat(response.json)))

    assert response.json == expected
    assert response.status == falcon.HTTP_OK


def test_get_single_book(client):
    expected = BOOKS[0]

    response = client.simulate_get('/books/%s' % expected['id'])

    logging.info("%s: %s" % (response.status, pformat(response.json)))

    assert response.json == expected
    assert response.status == falcon.HTTP_OK


# def test_post_image(client):
#     doc = {
#         'images': [
#             {
#                 'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
#             },
#             {
#                 'foo': 'bar'
#             }
#         ]
#     }
#
#     response = client.simulate_post('/images', json={'foo': 'bar'})
#     print response.json
#
#     assert response.json == doc
#     assert response.status == falcon.HTTP_201
