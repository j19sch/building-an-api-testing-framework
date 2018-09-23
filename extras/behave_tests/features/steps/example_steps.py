# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
import requests


@given('we got all the books')
def step_impl(context):
    response = requests.get("http://localhost:8000/books")
    context.books = response.json()


@given('we have valid credentials')
def step_impl(context):
    context.user = 'user'
    response = requests.post("http://localhost:8000/token/{}".format(context.user))
    context.token = response.json()['token']


@when('we delete one book')
def step_impl(context):
    context.response = requests.delete("http://localhost:8000/books/{}".format(context.books[0]['id']),
                                       headers={'User': context.user, 'Token': context.token})


@then('we get a 200 response')
def step_impl(context):
    assert context.response.status_code == 200, context.response.status_code


@then('the book is no longer present')
def step_impl(context):
    response = requests.get("http://localhost:8000/books/{}".format(context.books[0]['id']))
    assert response.status_code == 404
