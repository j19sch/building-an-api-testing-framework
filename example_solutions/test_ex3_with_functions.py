from example_solutions import apiclient_functions


def test_knockknock():
    response = apiclient_functions.knockknock()
    assert response.status_code == 200
    assert response.text == "Who's there?"


def test_get_all_books():
    response = apiclient_functions.get_all_books()
    assert response.status_code == 200
    books = response.json()
    assert books is not None
    assert len(books) == 5


def test_get_one_book():
    response = apiclient_functions.get_one_book('8b91b84b-04e4-4496-9635-66468c2f3e41')
    assert response.status_code == 200
    assert response.json() == {
        'id': '8b91b84b-04e4-4496-9635-66468c2f3e41',
        'title': 'Against Method',
        'sub_title': None,
        'author': 'Paul Feyerabend',
        'publisher': 'Verso',
        'year': 2010,
        'pages': 296
    }


def test_post_new_book():
    new_book = {
        "author": "Neil Gaiman",
        "pages": 299,
        "publisher": "W.W. Norton & Company",
        "sub_title": None,
        "title": "Norse Mythology",
        "year": 2017
    }

    response = apiclient_functions.post_book(new_book)
    assert response.status_code == 201
    assert response.json()['id'] is not None


def test_get_token_for_user():
    response = apiclient_functions.get_token('alice')
    print(response.status_code, response.json())
    assert response.status_code == 201
    assert response.json()['token'] is not None
