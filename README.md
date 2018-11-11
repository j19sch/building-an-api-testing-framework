# The "Books" API app - build an API testing framework in Python

**Disclaimer**: 
This app is intended as a practice app for a testing workshop, so I took some shortcuts. ;-)


## Setup & installation

If you run into any issues with the steps below, please let me know at j19sch@gmail.com.

### Python and VirtualEnv
- Install Python
    - Python 2.7 is fine. If you need to install Python, take Python 3 (it's the future).
    - Instructions: https://ehmatthes.github.io/pcc/chapter_01/README.html (no need to install Geany)
- Install virtualenv (`pip install --user virtualenv`)

### Setup a virtual environment
- Create a virtual python environment (`python -m virtualenv venv`)
	- Note that this will create the virtual environment in the current directory, so pick a convenient location.
	- If you have both Python 2.7 and Python 3 installed, and you want to use Python 3:
	`python -m virtualenv -p python3 venv`
- Activate virtualenv (linux, mac: `source venv/bin/activate`) or (win: `venv\Scripts\activate.bat`)
- Once you're done with the virtual environment (i.e. no longer want to play around with the code and the exercises), type `deactivate`
to deactivate it.

### Download and install this repo
- download this repository by clicking the green `Clone or download` button at the top (make sure you update to
the latest version right before the workshop) 
- Install requirements.txt (`pip install -r requirements.txt`)
- Install gunicorn (linux, mac: `pip install gunicorn`) or
waitress (win: `pip install waitress`)

### Running the app
- linux, mac: `gunicorn api_app.src.app` or win: `waitress-serve --port=8000 api_app.src.app:api`
- smoke test by using your browser to go to `localhost:8000/knockknock`
- the easiest way to restart the app is to kill the process (`ctrl/cmd+c`) and start it again

### Advaced text editor
- Any advanced text editor with the following features will do:
    - syntax highlighting (easier to read)
    - word completion (avoids typos in names of variables, functions and methods)
- If you're note sure which one to use, Visual Studio Code is a good choice: https://code.visualstudio.com/
You can find VS Code's Python plugin here: https://marketplace.visualstudio.com/items?itemName=ms-python.python 
- Using an IDE like PyCharm is fine too.



## Exercises  (`./exercises`)
See `./exercises/exercises_readme.md` for more information about the exercises.

### Reference materials
- API documentation for the app: `API-docs.md`
- Python cheatsheet
https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc.pdf
- Requests:
http://docs.python-requests.org/en/master/
- Pytest:
https://docs.pytest.org/en/latest/contents.html and https://docs.pytest.org/en/latest/reference.html



## Extras (`./extras`)

### next steps
- validating json with jsonschema
- test with parametrization
- debugging test code
- add a file handler to the logging

If you want even more options for logging, have a look at a pytest plugin I built: pytest-logfest at 
https://pypi.org/project/pytest-logfest/.

ToDo:
- Basic Auth instead of user/token in header (PATCH?)
- Reading data from files
- Pytest custom command-line options
- xml response
- SOAP API

### Same test, different tools
Test deleting a book, implemented with:
- behave: `behave <path>`
- pytest and requests: `pytest <path>`
- robot framework with robotframework-requests: `robot <path>`
- tavern: `pytest <path>`

ToDo: create book to delete in test, instead of deleting first on of retrieved books

### More Pytest
- Pytest Quick Start Guide - Bruno Oliveira
https://www.packtpub.com/web-development/pytest-quick-start-guide
- Python Testing with pytest: Simple, Rapid, Effective, and Scalable - Brian Okken
https://pragprog.com/book/bopytest/python-testing-with-pytest

### More Python
- Python koans: https://github.com/gregmalcolm/python_koans
- Raymond Hettinger - Transforming Code into Beautiful, Idiomatic
Python https://www.youtube.com/watch?v=OSGv2VnC0go
- James Powell - So you want to be a Python expert? https://www.youtube.com/watch?v=cKPlPJyQrt4



## Acknowledgements
- Mark Winteringham (@2bittester): restful-booker as inspiration
(https://github.com/mwinteringham/restful-booker)
- Eric Matthes for the Python Crash Course materials cheatsheet from the Python Crash Course
(https://ehmatthes.github.io/pcc/cheatsheets/README.html)
- Elizabeth Zagroba: tried it. More stuff works and is spelled correctly now.
- Everyone contributing to pytest, requests, falcon
