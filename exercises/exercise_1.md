## Exercise 1 - requests library
**Goal**: become familiar with the requests library  
**Purpose**: interacting programitically with an API

### Assignment
Print the status code and response for the following API calls:
- GET knockknock
- GET books
- GET one book
- POST a book
- POST auth

### The requests library
The requests library allows you to send API requests with `requests.get(url)`,
`requests.post(url, json=python_dict)`, etc.  
This will return a `response` object with (among other things) the following attributes:
- `response.status_code`
- `response.text`
- `response.json()` (json parsed to a Python dictionary)

Use `python <your_file>.py` to run your code.

Docs for the requests library: http://docs.python-requests.org/en/master/