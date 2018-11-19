## Exercise 6 - logging v2
**Goal**: add logging to record requests and responses  
**Purpose**: be able to see which requests and responses are being sent

### Assignment
Add logging to your API clients to capture information about requests and responses.

Since adding logging to each method of each API client is a lot of work to build and maintain,
an improvement on the solution of the previous exercise is to use the requests library's event hook
of the `requests.Session` class.

### requests.Session hook
The `requests.Session` class has a `hook` attribute containing a dictionary with only one key: `response`. The value for
that key is a list of methods or functions that are executed for every response. In this exercise you need to add a
method to that list to take care of the logging.

This class also allows you to send requests through its `get()`, `post()`, etc. methods. We will be using these
instead of what we've been doing so far, i.e. calling functions from the requests library directly.

To set all of this up in the most maintainable way, we need two levels of inheritance:
```
requests.Session, the Session class defined by the requests library
  |- a general ApiClient class, which takes care of the logging
    |- specific API client classes, one for reach API endpoint (`/books`, `/token`, etc,)
```

To the general ApiClient class you need to add the following `hook` setup :
```python
import requests 

class ApiClient(requests.Session):
    def __init__(self):
        super(ApiClient, self).__init__()  # initialises parent class; in Python 3: super().__init__()
        self.hooks['response'].append(self._log_details)  # for every response the _log_details() method will be called
        
    @staticmethod
    def _log_details(response, *args, **kwargs):
        pass  # you decide what kind of logging this should do ;-)
```

If you then have your specific API client classes inherit from this general ApiClient class, you can use `self.get()`
etc. to send requests, since they inherit these methods from their grandparent, the `requests.Session` class.

Docs: http://docs.python-requests.org/en/master/user/advanced/#event-hooks
Docs: http://docs.python-requests.org/en/master/api/#requests.Session