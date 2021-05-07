import falcon
from falcon import testing
import pytest

import uuid

from api_app.src.app import app
from api_app.src.data import BOOKS


@pytest.fixture
def client():
    return testing.TestClient(app)


@pytest.fixture
def get_user_and_token(client):
    user = 'Bob'
    response = client.simulate_post(f'/token/{user}')
    token = str(response.json['token'])

    return user, token


def test_get_books(client):
    expected = list(BOOKS)

    response = client.simulate_get('/books')

    assert response.status == falcon.HTTP_OK
    assert response.json == expected


def test_get_single_book(client):
    expected = BOOKS[0].copy()

    response = client.simulate_get(f'/books/{expected["id"]}')

    assert response.status == falcon.HTTP_OK
    assert response.json == expected


def test_get_single_book_invalid_uuid(client):
    invalid_uuid = 'invalid'
    response = client.simulate_get(f'/books/{invalid_uuid}')

    assert response.status == falcon.HTTP_BAD_REQUEST
    assert response.json['title'] == '400 Bad Request'
    assert response.json['description'] == 'Not a valid uuid.'


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
    assert response.status == falcon.HTTP_CREATED
    new_book["id"] = response.json['id']

    response = client.simulate_get(f'/books/{new_book["id"]}')
    assert response.status == falcon.HTTP_OK
    assert response.json == new_book


def test_post_book_invalid_request(client):
    new_book = {
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = client.simulate_post('/books', json=new_book)
    assert response.status == falcon.HTTP_BAD_REQUEST
    assert response.json['title'] == "Request data failed validation"
    assert response.json['description'] == "'author' is a required property"


def test_delete_book(client, get_user_and_token):
    book_to_delete = BOOKS[0].copy()
    user, token = get_user_and_token

    response = client.simulate_delete(f'/books/{book_to_delete["id"]}', headers={'User': user, 'Token': token})
    assert response.status == falcon.HTTP_OK

    response = client.simulate_get(f'/books/{book_to_delete["id"]}')
    assert response.status == falcon.HTTP_NOT_FOUND


def test_delete_nonexisting_book(client, get_user_and_token):
    user, token = get_user_and_token

    response = client.simulate_delete(f'/books/{uuid.uuid4()}', headers={'User': user, 'Token': token})

    assert response.status == falcon.HTTP_NOT_FOUND


def test_delete_book_no_auth(client):
    book_to_delete = BOOKS[0].copy()

    response = client.simulate_delete(f'/books/{book_to_delete["id"]}')
    assert response.status == falcon.HTTP_UNAUTHORIZED


def test_delete_book_wrong_user(client, get_user_and_token):
    book_to_delete = BOOKS[0].copy()
    user, token = get_user_and_token

    response = client.simulate_delete(f'/books/{book_to_delete["id"]}', headers={'User': 'notMe', 'Token': token})
    assert response.status == falcon.HTTP_UNAUTHORIZED


def test_delete_book_wrong_token(client, get_user_and_token):
    book_to_delete = BOOKS[0].copy()
    user, token = get_user_and_token

    response = client.simulate_delete(f'/books/{book_to_delete["id"]}', headers={'User': user, 'Token': 'wrong'})
    assert response.status == falcon.HTTP_UNAUTHORIZED


def test_delete_book_invalid_uuid(client, get_user_and_token):
    user, token = get_user_and_token

    invalid_uuid = 'invalid'
    response = client.simulate_delete(f'/books/{invalid_uuid}', headers={'User': user, 'Token': token})
    assert response.status == falcon.HTTP_BAD_REQUEST
    assert response.json['title'] == '400 Bad Request'
    assert response.json['description'] == 'Not a valid uuid.'


def test_put_book(client, get_user_and_token):
    book_to_update = BOOKS[0].copy()
    book_id = book_to_update.pop('id', None)

    user, token = get_user_and_token

    for key in book_to_update:
        book_to_update[key] = "foobar" if key in ['title', 'author'] else book_to_update[key]

    response = client.simulate_put(f'/books/{book_id}', json=book_to_update, headers={'User': user, 'Token': token})
    assert response.status == falcon.HTTP_OK
    book_to_update['id'] = book_id
    assert response.json == book_to_update


def test_put_nonexisting_book(client, get_user_and_token):
    book_to_update = BOOKS[0].copy()
    book_to_update.pop('id', None)
    book_id = uuid.uuid4()

    user, token = get_user_and_token

    for key in book_to_update:
        book_to_update[key] = "foobar" if key in ['title', 'author'] else book_to_update[key]

    response = client.simulate_put(f'/books/{book_id}', json=book_to_update, headers={'User': user, 'Token': token})
    assert response.status == falcon.HTTP_NOT_FOUND


def test_put_book_invalid_request(client, get_user_and_token):
    book_to_update = BOOKS[0].copy()
    book_id = book_to_update.pop('id', None)
    book_to_update.pop('author')

    user, token = get_user_and_token

    for key in book_to_update:
        book_to_update[key] = "foobar" if key in ['title', 'author'] else book_to_update[key]

    response = client.simulate_put(f'/books/{book_id}', json=book_to_update, headers={'User': user, 'Token': token})
    assert response.status == falcon.HTTP_BAD_REQUEST
    assert response.json['title'] == "Request data failed validation"
    assert response.json['description'] == "'author' is a required property"


def test_put_book_invalid_uuid(client, get_user_and_token):
    user, token = get_user_and_token

    invalid_uuid = 'invalid'
    response = client.simulate_put(f'/books/{invalid_uuid}', json={}, headers={'User': user, 'Token': token})
    assert response.status == falcon.HTTP_BAD_REQUEST
    assert response.json['title'] == '400 Bad Request'
    assert response.json['description'] == 'Not a valid uuid.'
