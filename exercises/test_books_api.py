import pytest
from . import books_client
from . import token_client

class TestBooksApi:
    client = books_client.Books()

    @pytest.fixture(scope="class")
    def fixture(self):
        return self.client.get_all()

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
        response = self.client.add_book(payload)
        response_body = response.json()
        id = response_body["id"]
        
        assert response_body is not None
        assert id is not None

        payload["id"] = id

        yield (response.status_code, response_body, payload)

        # teardown
        user = 'bob'
        tokenClient = token_client.Token()
        response = tokenClient.create_token(user)
        token = response.json()['token']
        response = self.client.delete_book(id, user, token)
        assert response.status_code == 200

    def test_status_code_is_ok(self, fixture):
        assert fixture.status_code == 200
    
    def test_books_contains_the_book(self, fixture):
        response_body = fixture.json()
        assert len(response_body) > 0

    def test_book_store_request_is_successful(self, post_fixture):
        status_code, _, _ = post_fixture
        assert status_code == 201

    def test_book_is_stored(self, post_fixture):
        _, response_body, payload = post_fixture

        respponse = self.client.get_book(response_body["id"])
        response_body = respponse.json()
        assert response_body is not None
        assert response_body == payload
