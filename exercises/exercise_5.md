
## Exercise 5 - logging

**Goal**: add logging so you can debug more easily

### Assignment
Add logging to your tests by using the requests hook.

### Logging
To create log records, you'll need to import the logging module. After that you can easily create log records of 
different log levels, e.g. `logging.info("all good")` or `logging.critical("run away!")`

When a test results in an error or a fail, pytest will automatically output the created log records. If you want to
see the log records regardless of test result, use `pytest --log-cli-level debug`.

Docs:
- https://docs.python.org/2/library/logging.html
- https://docs.python.org/3/library/logging.html
- https://docs.pytest.org/en/latest/logging.html


### Requests hook
The `requests.Session` object has a `hook` attribute containing a dictionary with only one key: `response`.
The value for that key is a list of functions that are run for every response.    
By adding the name of a function to that list in the `__init__` of a subclass of `requests.session`,
 you can use that function to take care of the logging of each request and response.
 
Useful attributes of the `repsonse` object:
- `response.status_code`
- `response.headers`
- `response.text`
- `response.json()` (json parsed to a Python dictionary)
- `repsonse.request.url`
- `repsonse.request.method`
- `repsonse.request.headers`
- `repsonse.request.body`

Docs: http://docs.python-requests.org/en/master/user/advanced/#event-hooks
