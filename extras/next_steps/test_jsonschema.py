import jsonschema
import requests

# The three dictionaries below define json schema's, which are used in the tests to check the format of the responses.
# Json schema docs: https://python-jsonschema.readthedocs.io/en/latest/
#
# For validating responses with the Schema library, see test_schema_validation.


book_definition = {
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
    "required": ["title", "sub_title", "author", "publisher", "year", "pages"],
    "additionalProperties": "false"
}

schema_book = book_definition

schema_books = {
    "type": "array",
    "items": book_definition
}


def test_get_book():
    response = requests.get('http://localhost:8000/books/8b91b84b-04e4-4496-9635-66468c2f3e41')

    assert response.status_code == 200
    jsonschema.validate(response.json(), schema_book)


def test_get_books():
    response = requests.get('http://localhost:8000/books')

    assert response.status_code == 200
    jsonschema.validate(response.json(), schema_books)
