
## Exercise 4 - fixtures
**Goal**: use fixtures for test setup and teardown

### Assignment
Create a test using fixtures in which you:
- get a token
- create a book
- delete that book

### Fixtures
Pytest allows you to define fixtures for test setup and teardown using the `@pytest.fixture` decorator.
Not only tests can use fixtures, fixtures can also use other fixtures.

Example:
```
@pytest.fixture
def my_favourite_number():
    return 73
    
def test_my_favourite_number_is_73(my_favourite_number):
    assert my_favourite_number == 73
```

Docs: https://docs.pytest.org/en/latest/fixture.html