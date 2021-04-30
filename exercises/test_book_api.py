import pytest
from . import books_client
from . import token_client

class TestBookApi:
    books_api = books_client.Books()
    token_api = token_client.Token()
    
    @pytest.fixture(scope="class")
    def creds(self):
        user = 'bob'
        response = self.token_api.create_token(user)
        token = response.json()['token']
        return user, token

    @pytest.fixture(scope="class")
    def new_book(self, creds):
        # setup
        payload = {
            'title': 'New book',
            'sub_title': 'New book sub title',
            'author': 'Dmytro Titenko',
            'publisher': 'Mendix',
            'year': 2021,
            'pages': 53
        }
        response = self.books_api.add_book(payload)
        assert response.status_code  == 201

        response_body = response.json()
        assert response_body is not None
        
        id = response_body["id"]
        assert id is not None
        payload["id"] = id

        yield self.books_api.get_book(id), payload

        # teardown
        user, token = creds
        response = self.books_api.delete_book(id, user, token)
        assert response.status_code == 200

    def test_status_code_is_ok(self, new_book):
        response, _ = new_book
        assert response.status_code == 200
    
    def test_book_has_correct_title(self, new_book):
        response, payload = new_book
        response_body = response.json()
        assert response_body == payload
