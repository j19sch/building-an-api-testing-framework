# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
import requests


@given('we have posted an image')
def step_impl(context):
    requests.post("http://localhost:8000/images", json={"foo": "bar"})


@when('we retrieve the image')
def step_impl(context):
    response = requests.get("http://localhost:8000/images")
    context.response = response


@then('we get both the existing and the newly posted image')
def step_impl(context):
    assert context.response.status_code == 201
    assert context.response.text == '{"images": [{"href": "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png"}, {"foo": "bar"}]}'
