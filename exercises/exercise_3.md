## Exercise 3 - fixtures
**Goal**: use fixtures for test setup and teardown  
**Purpose**: separate setup & teardown from the tests (separation of concerns,
don't repeat yourself)

### Assignment
Create a test where you use fixtures to:
- create a token
- create a book

after which the test will:
- delete that book

The token is needed to successfully make the delete call. It simulates APIs that require authentication via e.g. BasicAuth
or JWTs. "Simulates" because the implementation here is not secure in any way. However, it successfully requires you to
provide a valid token for some of the API calls, which is good enough for these exercises.


### Fixtures
Pytest allows you to define fixtures for test setup and teardown using the
`@pytest.fixture` decorator. In this exercise we will only look at using fixtures
to set up data. To see an example of a teardown fixture, see
`test_setup_teardown_fixture.py` in `./extras/next_steps`.

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

Fixtures can apply to different levels of your tests:
- `function` is limited to a particular test (default)
- `module` is limited to a particular file
- `session` is executed once for all the tests you're running
Here's how you'd modify your fixture decorator to limit the fixture to one test:
`@pytest.fixture(scope="function")`.

Note that not only tests can use fixtures, fixtures can also use other fixtures.

Docs: https://docs.pytest.org/en/latest/fixture.html  


### Requests library - headers
To make the delete call, you will need to add headers to your request. This can be done as follows:  
`response = requests.delete(<url>, headers={'user': <user>, 'token': <token>})`