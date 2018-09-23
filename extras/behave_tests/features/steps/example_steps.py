# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
import requests


@given('we got all the books')
def step_impl(context):
    response = requests.get("http://localhost:8000/books")
    context.books = response.json()


@when('we retrieve one book')
def step_impl(context):
    book_id = context.books[0]['id']
    response = requests.get("http://localhost:8000/books/%s" % book_id)
    context.response = response


@then('we get just the one book')
def step_impl(context):
    assert context.response.status_code == 200
    assert context.response.json() == context.books[0]
