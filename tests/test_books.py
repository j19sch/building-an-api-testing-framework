import falcon
from falcon import testing
import pytest

from api_app.app import api
from api_app.data import BOOKS


@pytest.fixture(scope='function')
def client():
    return testing.TestClient(api)


def test_get_books(client):
    expected = list(BOOKS)

    response = client.simulate_get('/books')

    assert response.status == falcon.HTTP_OK
    assert response.json == expected


def test_get_single_book(client):
    expected = BOOKS[0].copy()

    response = client.simulate_get('/books/%s' % expected['id'])

    assert response.status == falcon.HTTP_OK
    assert response.json == expected


def test_post_book(client):
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = client.simulate_post('/books', json=new_book)
    new_book["id"] = response.json['id']
    assert response.status == falcon.HTTP_CREATED

    response = client.simulate_get('/books/%s' % new_book['id'])
    assert response.status == falcon.HTTP_OK
    assert response.json == new_book


def test_delete_book(client):
    book_to_delete = BOOKS[0].copy()

    response = client.simulate_delete('/books/%s' % book_to_delete["id"])
    assert response.status == falcon.HTTP_OK

    response = client.simulate_get('/books/%s' % book_to_delete["id"])
    assert response.status == falcon.HTTP_NOT_FOUND


def test_put_book(client):
    book_to_update = BOOKS[0].copy()
    book_id = book_to_update.pop('id', None)

    for key in book_to_update:
        book_to_update[key] = "foobar" if key != "id" else book_to_update[key]

    response = client.simulate_put('/books/%s' % book_id, json=book_to_update)
    assert response.status == falcon.HTTP_OK
    book_to_update['id'] = book_id
    assert response.json == book_to_update
