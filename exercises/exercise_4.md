## Exercise 4 - API clients
**Goal**: build an interface between the API and your tests  
**Purpose**: separate the test code from the API code (separation of concerns,
don't repeat yourself)

### Assignment
Create an API client module as an abstraction layer (or interface) between the API and your tests.  

You could do this using either functions or classes.
However, because of something we want to do in exercise 5, you should use classes.


### Apiclient class
You can define a class as follows:
```
class MyClass(object):  # def MyClass(): in Python 3
    def __init__(self):
        pass  # this code is run when instantiating the class
    
    def my_method(self):
        pass  # this code is run with my_class = MyClass(); my_class.my_method()

```

Docs:
- https://docs.python.org/3/tutorial/classes.html
- https://docs.python.org/2/tutorial/classes.html
