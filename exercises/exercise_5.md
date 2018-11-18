## Exercise 5 - logging
**Goal**: add logging to record requests and responses  
**Purpose**: be able to see which requests and responses are being sent

### Assignment
Add logging to your tests by using the requests hook.

### Logging
To create log records, you'll need to import the logging module. After that you can easily create
log records of different log levels, e.g. `logging.info("all good")` or `logging.critical("run away!")`

When a test results in an error or a fail, pytest will automatically output the created log records.
If you want to see the log records regardless of the test result, use `pytest --log-cli-level debug`.

Docs:
- https://docs.python.org/2/library/logging.html
- https://docs.python.org/3/library/logging.html
- https://docs.pytest.org/en/latest/logging.html


### Requests hook
The `requests.Session` class has a `hook` attribute containing a dictionary with only
one key: `response`. The value for that key is a list of functions that are run for every response.    

By adding the name of a function to that list in the `__init__` of a subclass of `requests.Session`,
you can use that function to take care of the logging of each request and response:
```python
import requests 

class ApiClient(requests.Session):
    def __init__(self):
        super(ApiClient, self).__init__()  # super().__init__() in Python3
        self.hooks['response'].append(self._log_details)
        
    @staticmethod
    def _log_details(response, *args, **kwargs):
        pass  # you decide what this should do ;-)
```

So you end up with two levels of inheritance:
```
requests.Session, the Session class defined by the requests library
  |- general ApiClient class, takes care of the logging
    |- specific API client classes, one for reach API endpoint (`/books`, `/token`, etc,)
```

Docs: http://docs.python-requests.org/en/master/user/advanced/#event-hooks


### Requests library - response object
The `response` object has several interesting attributes for logging purposes:
- `response.status_code`
- `response.headers`
- `response.text`
- `response.json()` (json parsed to a Python dictionary)
- `response.request.url`
- `response.request.method`
- `response.request.headers`
- `response.request.body`

Docs: http://docs.python-requests.org/en/master/api/#requests.Response