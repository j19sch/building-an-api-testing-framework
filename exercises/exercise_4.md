## Exercise 4 - API clients
**Goal**: build an interface between the API and your tests  
**Purpose**: separate the test code from the API code (separation of concerns,
don't repeat yourself)

### Assignment
Create an API client module as an abstraction layer (or interface) between the API and your tests. You could do this
using either functions or classes. However, because of something we want to do in exercise 5, you should use classes.

The module should contain one class per endpoint of the API - with your tests calling the methods of that class
to interact with the APIs.


### Using code from another file
To be able to use code from the API client module in the file with your tests, you'll need to `import` it. To keep
things as simple as possible for this exercise, you can do the following:

- In the same directory as the files with your tests, create a file called `api_clients.py`. This will be the module
containing the API client (see next section).
- In that same directory, create an empty file called `__init__.py`. This tells Python you want to import code from
this directory.
- At the top of your file with tests, add `from . import api_clients`.

### Apiclient class
You can define a class as follows:
```python
import requests

class MyClass:
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
```python
from . import api_clients

def test_with_a_class():
    my_class = api_clients.MyClass()
    response = my_class.my_method()

```

Docs:
- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/3/tutorial/modules.html#importing-from-a-package
