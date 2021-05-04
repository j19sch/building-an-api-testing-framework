import pytest
from uuid import UUID
from schema import And, Or, Schema

from . import books_client
from . import token_client


class TestBooksApi:
    client = books_client.Books()

    def validate_uuid_v4(self, uuidv4):
        try:
            UUID(uuidv4, version=4)
        except ValueError:
            return False
        else:
            return True

    @pytest.fixture(scope="class")
    def get_all(self):
        return self.client.get_all()

    @pytest.fixture(scope="class")
    def creds(self):
        user = 'bob'
        tokenClient = token_client.Token()
        response = tokenClient.create_token(user)
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
        response = self.client.add_book(payload)
        response_body = response.json()
        id = response_body["id"]

        assert response_body is not None
        assert id is not None

        payload["id"] = id

        yield (response.status_code, response_body, payload)

        # teardown
        user, token = creds
        response = self.client.delete_book(id, user, token)
        assert response.status_code == 200

    @pytest.fixture(scope="class")
    def schema_book(self):
        return {
            'id': And(str, self.validate_uuid_v4),
            'title': str,
            'sub_title':  Or(None, str),
            'author': And(str, lambda s: len(s.strip()) > 0),
            'publisher': str,
            'year': int,
            'pages': And(int, lambda i: i > 0)
        }

    @pytest.fixture(scope="class")
    def schema_books(self, schema_book):
        return Schema([schema_book])

    def test_status_code_is_ok(self, get_all):
        assert get_all.status_code == 200

    def test_books_contains_the_book(self, get_all):
        response_body = get_all.json()
        assert len(response_body) > 0

    def test_book_store_request_is_successful(self, new_book):
        status_code, _, _ = new_book
        assert status_code == 201

    def test_book_is_stored(self, new_book):
        _, response_body, payload = new_book

        respponse = self.client.get_book(response_body["id"])
        response_body = respponse.json()
        assert response_body is not None
        assert response_body == payload

    def test_response_should_have_valid_schema(self, get_all, schema_books):
        response_body = get_all.json()
        schema_books.validate(response_body)
