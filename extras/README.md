# Extras

## Next steps

The `next_steps` directory contains several options for extending your test framework:
- `debugging.md`: explains how to use the Python debugger with pytest
- `test_jsonschema.py`: validation json with the jsonschema libary
- `test_log_to_file.py`: write your test logs to a file
- `test_parametrization.py`: uses pytest's parametrization to run the same test with different inputs
- `test_teardown_fixture.py`: uses the `yield` statement in a fixture to execute teardown

If you want even more options for logging, have a look at a pytest plugin I built: pytest-logfest at 
https://pypi.org/project/pytest-logfest/.


## Same test, different tools
The `same_test_different_tools` directory contains the same test (deleting a book) implemented
using different tools:
- behave: run with `behave <path>`
- pytest and requests: run with `pytest <path>`
- robot framework with robotframework-requests:  run with `robot <path>`
- tavern:  run with  `pytest <path>`


ToDo:
- create book to delete in test, instead of deleting first one of retrieved books
