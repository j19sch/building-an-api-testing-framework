import requests

_BASE_URL = 'http://localhost:8000'


def knockknock():
    return requests.get(_BASE_URL + '/knockknock')


def get_all_books():
    return requests.get(_BASE_URL + '/books')


def get_one_book(book_id):
    return requests.get(_BASE_URL + '/books' + '/' + book_id)


def post_book(new_book):
    return requests.post(_BASE_URL + '/books', json=new_book)


def get_token(username):
    return requests.post(_BASE_URL + '/token' + '/' + username)


# part of exercise 4
def delete_book(book_id, user, token):
    return requests.delete(_BASE_URL + '/books' + '/' + book_id, headers={'user': user, 'token': token})
