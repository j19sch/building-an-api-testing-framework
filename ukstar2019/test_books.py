import uuid


def test_get_books(books_api, initial_books):
    expected = list(initial_books)

    response = books_api.get_all_books()

    assert response.status_code == 200
    assert response.json() == expected


def test_get_single_book(books_api, initial_books):
    expected = initial_books[0].copy()

    response = books_api.get_one_book(expected['id'])
    assert response.status_code == 200
    assert response.json() == expected


def test_get_single_book_invalid_uuid(books_api):
    response = books_api.get_one_book("invalid")

    assert response.status_code == 400
    assert response.json()['title'] == '400 Bad Request'
    assert response.json()['description'] == 'Not a valid uuid.'


def test_post_book(books_api):
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = books_api.post_book(new_book)
    assert response.status_code == 201
    new_book["id"] = response.json()['id']

    response = books_api.get_one_book(new_book['id'])
    assert response.status_code == 200
    assert response.json() == new_book


def test_post_book_invalid_request(books_api):
    new_book = {
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = books_api.post_book(new_book)
    assert response.status_code == 400
    assert response.json()['title'] == "Failed data validation"
    assert response.json()['description'] == "'author' is a required property"


def test_delete_book(books_api, initial_books, creds, new_book):
    book_to_delete = new_book['id']
    user, token = creds

    response = books_api.delete_book(book_to_delete, user, token)
    assert response.status_code == 200

    response = books_api.get_one_book(book_to_delete)
    assert response.status_code == 404


def test_delete_nonexisting_book(books_api, creds):
    user, token = creds
    book_id = str(uuid.uuid4())

    response = books_api.delete_book(book_id, user, token)
    assert response.status_code == 404


def test_delete_book_no_auth(books_api, new_book):
    book_to_delete = new_book

    response = books_api.delete_book(book_to_delete['id'], None, None)
    assert response.status_code == 401


def test_delete_book_invalid_auth(books_api, creds, new_book):
    book_to_delete = new_book
    user, token = creds

    response = books_api.delete_book(book_to_delete['id'], user, 'wrong')
    assert response.status_code == 401


def test_delete_book_invalid_uuid(books_api, creds):
    user, token = creds

    response = books_api.delete_book("invalid", user, token)
    assert response.status_code == 400
    assert response.json()['title'] == '400 Bad Request'
    assert response.json()['description'] == 'Not a valid uuid.'


def test_update_book(books_api, creds, new_book):
    book_to_update = new_book
    book_id = book_to_update.pop('id', None)

    user, token = creds

    for key in book_to_update:
        book_to_update[key] = "foobar" if key in ['title', 'author'] else book_to_update[key]

    response = books_api.update_book(book_id, book_to_update, user, token)
    assert response.status_code == 200
    book_to_update['id'] = book_id
    assert response.json() == book_to_update


def test_update_nonexisting_book(books_api, creds, new_book):
    book_to_update = new_book
    book_to_update.pop('id', None)
    book_id = str(uuid.uuid4())

    user, token = creds

    for key in book_to_update:
        book_to_update[key] = "foobar" if key in ['title', 'author'] else book_to_update[key]

    response = books_api.update_book(book_id, book_to_update, user, token)
    assert response.status_code == 404


def test_update_book_invalid_request(books_api, creds, new_book):
    book_to_update = new_book
    book_id = book_to_update.pop('id', None)
    book_to_update.pop('author')

    user, token = creds

    for key in book_to_update:
        book_to_update[key] = "foobar" if key in ['title', 'author'] else book_to_update[key]

    response = books_api.update_book(book_id, book_to_update, user, token)
    assert response.status_code == 400
    assert response.json()['title'] == "Failed data validation"
    assert response.json()['description'] == "'author' is a required property"


def test_update_book_invalid_uuid(books_api, creds):
    user, token = creds

    response = books_api.update_book("invalid", {}, user, token)
    assert response.status_code == 400
    assert response.json()['title'] == '400 Bad Request'
    assert response.json()['description'] == 'Not a valid uuid.'
