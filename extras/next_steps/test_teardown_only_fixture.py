import pytest
import requests


# A teardown-only fixture requires a little creativity with pytest's fixtures. The trick is to
# make the fixture yield a list and have the test add the things you want to teardown to that
# list. After the test completes, the fixture will run the code after the yield.
#
# To make sure the teardown happens, it's best to update the fixture's list as soon as possible.
# If for example you do it at the end of the test, any failing assert means the list does not get
# updated and the teardown is not executed for the item that would be added at the end of the test.


@pytest.fixture
def books_to_delete():
    books_to_delete = []
    yield books_to_delete

    for book in books_to_delete:
        user = 'bob'
        response = requests.post(f'http://localhost:8000/token/{user}')
        token = response.json()['token']
        response = requests.delete(f'http://localhost:8000/books/{book}',
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

    # ToDo: add additional asserts/validatrions here
