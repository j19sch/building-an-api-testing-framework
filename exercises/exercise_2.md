## Exercise 2 - pytest
**Goal**: become familiar with pytest  
**Purpose**: running tests

### Assignment
Build tests for the API calls of exercise 1.

Make sure you have seen output of the following cases:
- test passes
- test fails
- test throws error, e.g. because of a bug in the test

### Pytest
Pytest will collect tests based on the following criteria:
- current directory and all sub-directories
- files named `test_*.py` or `*_test.py`
- functions named `test_*`

To run the tests, execute `pytest` in the directory containing your tests,
or specify the path: `pytest <path_to_dir>`.

You can use `assert a  == b` to check the actual value against the expected value.
In general it's not needed to add an assert message, since Pytest does a great job
reporting on failed tests.

Docs: https://docs.pytest.org/en/latest/getting-started.html#create-your-first-test