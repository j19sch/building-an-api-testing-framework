import requests
import pytest

class TestBooksApi:
    @pytest.fixture(scope="class")
    def fixture(self):
        return requests.get('http://localhost:8000/books')

    @pytest.fixture(scope="class")
    def post_fixture(self):
        # setup
        payload = {
            'title': 'New book',
            'sub_title': 'New book sub title',
            'author': 'Dmytro Titenko',
            'publisher': 'Mendix',
            'year': 2021,
            'pages': 53
        }
        response = requests.post('http://localhost:8000/books', json=payload)
        response_body = response.json()
        id = response_body["id"]
        
        assert response_body is not None
        assert id is not None

        payload["id"] = id

        yield (response.status_code, response_body, payload)

        # teardown
        user = 'bob'
        response = requests.post(f'http://localhost:8000/token/{user}')
        token = response.json()['token']
        response = requests.delete(f'http://localhost:8000/books/{id}', headers={'user': user, 'token': token})
        assert response.status_code == 200

    def test_status_code_is_ok(self, fixture):
        assert fixture.status_code == 200
    
    def test_books_contains_the_book(self, fixture):
        response_body = fixture.json()
        assert response_body[0]['id'] == '9b30d321-d242-444f-b2db-884d04a4d806'

    def test_book_store_request_is_successful(self, post_fixture):
        status_code, _, _ = post_fixture
        assert status_code == 201

    def test_book_is_stored(self, post_fixture):
        _, response_body, payload = post_fixture

        respponse = requests.get(f'http://localhost:8000/books/{response_body["id"]}')
        response_body = respponse.json()
        assert response_body is not None
        assert response_body == payload
