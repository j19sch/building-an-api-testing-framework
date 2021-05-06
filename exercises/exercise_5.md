## Exercise 5 - logging v1
**Goal**: add logging to record requests and responses  
**Purpose**: be able to see which requests and responses are being sent

### Assignment
Add logging to your API clients to capture information about requests and responses.

For this assignment it is sufficient to add logging to the `POST` on `/books` in the setup of your test.
In the next exercise, we will look at a more generic and more maintainable way to log requests and responses.


### Logging
To create log records, you'll need to import the logging module. After that you can easily create
log records of different log levels, e.g. `logging.info("all good")` or `logging.critical("run away!")`

When a test results in an error or a fail, pytest will automatically output log records that were created
on level `WARNING` and higher. If you want to see all log records of level `INFO` and higher (so no `DEBUG`)
regardless of the test result, use `pytest --log-cli-level info`.

Docs:
- https://docs.python.org/2/library/logging.html
- https://docs.python.org/3/library/logging.html
- https://docs.pytest.org/en/latest/logging.html


### Requests library - response object
All the HTTP methods of the requests library (`requests.get()`, `requests.post()`, etc.) return a response object.
This object contains all the information we need for logging purposes:
- `response.status_code`
- `response.headers`
- `response.text`
- `response.json()` (json parsed to a Python dictionary)
- `response.request.url`
- `response.request.method`
- `response.request.headers`
- `response.request.body`

Docs: http://docs.python-requests.org/en/master/api/#requests.Response

### Reports
Pytest does not have a built-in formatted report beyond what you've seen
in the console. The `pytest-html` library allows you to generate an HTML
report.

Docs: https://pypi.org/project/pytest-html/
