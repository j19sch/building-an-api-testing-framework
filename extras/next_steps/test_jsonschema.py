import jsonschema
import requests


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
    "required": ["title", "sub_title", "author", "publisher", "year", "pages"]
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
