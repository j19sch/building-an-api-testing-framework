## Exercise 4 - API clients
**Goal**: build an interface between the API and your tests  
**Purpose**: separate the test code from the API code (separation of concerns,
don't repeat yourself)

### Assignment
Create an API client module as an abstraction layer (or interface) between the API and your tests. You could do this
using either functions or classes. However, because of something we want to do in exercise 5, you should use classes.

The module should contain one class per endpoint of the API - with your tests calling the methods of that class
to interact with the APIs.


### Apiclient class
You can define a class as follows:
```python
import requests

class MyClass(object):  # class MyClass(): in Python 3
    def __init__(self):
        # this code is run when instantiating the class my_class = MyClass()
        # one thing you can do here, is store the endpoint of the url:
        self.url = "http://localhost:8000/knockknock"
    
    def my_method(self):
        # this code is run for an instance with my_class.my_method()
        # so if we want to the GET of our smoketest:
        return requests.get(self.url)

```

And then use it in a test:
```
def test_with_a_class():
    my_class = MyClass()
    response = my_class.my_method()

```

Docs:
- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/2/tutorial/classes.html
