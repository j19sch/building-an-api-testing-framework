## Exercise 2 - pytest
**Goal**: become familiar with pytest  
**Purpose**: building and running tests

### Assignment
Build tests for the API calls of exercise 1.

Make sure you have seen output of the following cases:
- test passes, i.e. the assert evaluates to `True`
- test fails, i.e. the assert evaluates to `False`
- test throws error, e.g. because of a bug in the test

### Pytest
Pytest will collect tests based on the following criteria:
- search the current directory and all sub-directories
- for files named `test_*.py` or `*_test.py`
- that contain functions named `test_*`

To run the tests, execute `pytest` in the directory containing your tests,
or specify the path: `pytest <path_to_dir>`.

You can use `assert a == b` to check actual values against expected values.
In general it's not needed to add an assert message, since Pytest does a great job
reporting on failed tests. If you do want an assert message: `assert a == b, "a did not equal b"`
or `assert a == b, "value of a: {} does not equal value of b: {}".format(a, b)`

Docs: https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test