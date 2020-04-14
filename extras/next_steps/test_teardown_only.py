import pytest
import requests


@pytest.fixture
def books_to_delete():
    books_to_delete = []
    yield books_to_delete

    for book in books_to_delete:
        user = 'bob'
        response = requests.post('http://localhost:8000/token/' + user)
        token = response.json()['token']
        response = requests.delete('http://localhost:8000/books/' + book,
                                   headers={'user': user, 'token': token})
        assert response.status_code == 200


def test_create_a_book(books_to_delete):
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = requests.post('http://localhost:8000/books', json=new_book)
    assert response.status_code == 201

    books_to_delete.append(response.json()['id'])
