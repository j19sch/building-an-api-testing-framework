from uuid import UUID

import requests
from schema import And, Or, Schema


# The response validations in these two tests are done with the Schema libary: https://pypi.org/project/schema/
# The book dictionary below is not written for optimal coverage, but to show different options with the library.
#
# For validating responses against a jsonschema, see test_jsonschema.


def validate_uuid_v4(uuidv4):
    try:
        UUID(uuidv4, version=4)
    except ValueError:
        return False
    else:
        return True


book = {
    'id': And(str, validate_uuid_v4),
    'title': str,
    'sub_title':  Or(None, str),
    'author': And(str, lambda s: len(s.strip()) > 0),
    'publisher': str,
    'year': int,
    'pages': And(int, lambda i: i > 0)
}

book_schema = Schema(book)
books_schema = Schema([book])


def test_get_book():
    response = requests.get('http://localhost:8000/books/8b91b84b-04e4-4496-9635-66468c2f3e41')

    assert response.status_code == 200
    book_schema.validate(response.json())


def test_get_books():
    response = requests.get('http://localhost:8000/books')

    assert response.status_code == 200
    books_schema.validate(response.json())
