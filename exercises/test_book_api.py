import pytest
import jsonschema
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
        assert response.status_code == 201

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

    @pytest.fixture(scope="class")
    def schema_book(self):
        schema = {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string"
                },
                "sub_title": {
                    "type": ["string", "null"],
                },
                "author": {
                    "type": "string"
                },
                "publisher": {
                    "type": "string"
                },
                "year": {
                    "type": "integer"
                },
                "pages": {
                    "type": "integer"
                }
            },
            "required": ["title", "sub_title", "author", "publisher", "year", "pages"]
        }
        return schema

    def test_status_code_is_ok(self, new_book):
        response, _ = new_book
        assert response.status_code == 200

    def test_book_has_correct_title(self, new_book):
        response, payload = new_book
        response_body = response.json()
        assert response_body == payload

    def test_response_has_valid_schema(self, new_book, schema_book):
        response, _ = new_book
        response_body = response.json()
        jsonschema.validate(response_body, schema_book)

    @pytest.mark.parametrize("invalid_book_id, why_invalid", [
        ("is one number string", "1"),
        ("is a set of random characters", "aaaa"),
        ("last character missing", "11d399cb-5a44-430c-bb9d-51fa3dab986"),
        ("has 'h' at the beginning which makes uuid invalid", "h1d399cb-5a44-430c-bb9d-51fa3dab9864")
    ])
    def test_should_return_bad_request_if_id_(self, why_invalid, invalid_book_id):
        response = self.books_api.get_book(invalid_book_id)
        assert response.status_code == 400
        assert response.json()['title'] == '400 Bad Request'
        assert response.json()['description'] == 'Not a valid uuid.'
