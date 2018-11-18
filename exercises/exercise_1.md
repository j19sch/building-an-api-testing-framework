## Exercise 1 - requests library
**Goal**: become familiar with the requests library  
**Purpose**: interacting programmatically with an API

### Assignment
Print the status code and response for the following API calls:
- GET knockknock
- GET books
- GET one book
- POST a book
- POST token

You can find a description of the APIs in `API-docs.md`.

Don't forget to explore and generate some error responses.     

### The requests library
The requests library allows you to send API requests with `requests.get(<url>)`,
`requests.post(url, json=<python_dictionary>)`, etc.  
This will return a `response` object with (among other things) the following attributes:
- `response.status_code`: http status code of the response
- `response.text`: the response body as plain text
- `response.json()`: parses a json response body to a Python dictionary

To perform the smoke test from the setup instructions in Python:
```python
import requests

response = requests.get('http://localhost:8000/knockknock')
print(response.status_code)
print(response.text)
```

So to get started, create a new file in the `exercises` folder, copy-paste the above example into it,
and run it with `python <your_file>.py`.

Docs for the requests library: http://docs.python-requests.org/en/master/


### Printing text to the screen
To print text to the screen, use `print(<string>)`.  
If you need string interpolation, use the `format()` function:
`print("value a is {}, value of b is {}".format(a, b))`  

To make printed dictionaries (and other data structures) more readable, use `pprint`:  
```
from pprint import pprint
pprint(<dictionary>)
```

And if you want to combine pretty-printing with string interpolation:
```
from pprint import pformat
print("dictionary: {}".format(pformat(<dictionary>)))
```
