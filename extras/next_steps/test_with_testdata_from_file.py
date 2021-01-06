import pytest
import requests
import yaml  # package name when installing is pyyaml


# The fixture below will open the testdata.yml file and parse it with pyyaml. The result is a Python dictionary
# which is used in the test to create a book.
# Using the `with` keyword when dealing with files, is a good practice: it makes sure that the file is properly
# closed, even if exceptions are raised.
#
# PyYAML docs: https://pyyaml.org/wiki/PyYAMLDocumentation
# Python docs on files: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files and
#     https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files and


@pytest.fixture
def test_data():
    with open('./extras/next_steps/testdata.yml') as testdata:
        return yaml.full_load(testdata)


def test_something(test_data):
    response = requests.post('http://localhost:8000/books', json=test_data['books']['book_1'])
    assert response.status_code == 201
    assert response.json()['id'] is not None
