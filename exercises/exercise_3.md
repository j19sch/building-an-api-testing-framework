## Exercise 3 - fixtures
**Goal**: use fixtures for test setup and teardown  
**Purpose**: separate setup & teardown from the tests (separation of concerns,
don't repeat yourself)

### Assignment
Create a test where you use fixtures to:
- get a token
- create a book

after which the test will:
- delete that book


### Fixtures
Pytest allows you to define fixtures for test setup and teardown using the
`@pytest.fixture` decorator. In this exercise we will only look at using fixtures
to set up data. (If you're curious about teardown, so below for a link to the relevant documentation.)

To create a fixture, write a function and add the `@pytest.fixture` decorator to that function.
Any test function can then use the return value(s) of your fixture, by using the function's name
as an argument for the test function:
```python
import pytest

@pytest.fixture
def my_favourite_number():
    return 73
    
def test_my_favourite_number_is_73(my_favourite_number):
    assert my_favourite_number == 73
```

Note that not only tests can use fixtures, fixtures can also use other fixtures.

Docs: https://docs.pytest.org/en/latest/fixture.html  
Docs - teardown: https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code


### Requests library - headers
To make the delete call, you will need to add headers to your request. This can be done as follows:  
`response = requests.delete(<url>, headers={'user': <user>, 'token': <token>})`