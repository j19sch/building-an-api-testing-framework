# API app

### Disclaimer
This app is intended as a practice app for a testing workshop, so I took some shortcuts. ;-)

## Setup & installation and running the app

### Setup & installation

#### Python and VirtualEnv
- Install Python
    - Python 2.7 is fine, If you're going to install, take Python 3 (it's the future).
    - Instructions: https://ehmatthes.github.io/pcc/chapter_01/README.html (do not install Geany)
- Install virtualenv (`pip install --user virtualenv` or `pip3 install --user virtualenv`)
- Advanced text editor (Visual Studio Code (https://code.visualstudio.com/) is a good choice if you're not sure.)

#### Setup a virtual environment
- Create virtualenv (`virtualenv venv` or `virtualenv -p python3 venv`)
- Activate virtualenv (`source venv/bin/activate` or `venv\bin\activate.bat`)

#### Download and install this repo
- download this repository (download the zip file or `git clone`)
- Install requirements.txt (`pip|pip3 install -r requirements.txt`)
- Install gunicorn (linux, mac: `pip|pip3 install gunicorn`) or waitress (win: `pip|pip3 install waitress`)

### Running the app
- `gunicorn api_app.src.app` (linux, mac) or `waitress-serve --port=8000 api_app:src:app` (win)
- smoke test by sending a GET request to `localhost:8000/knockknock`, e.g. with httpie: `http -v localhost:8000/knockknock`


## Reference materials
- Python cheatsheet https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc.pdf
- Requests: http://docs.python-requests.org/en/master/
- Pytest: https://docs.pytest.org/en/latest/contents.html and https://docs.pytest.org/en/latest/reference.html


## Exercises
- see `API-DOCS.md` for a description of the API
- do exercises
- play around
- check `example_solutions` for a good way to solve the exercise

### Exercise 1 - Requests library
Goal: send a GET request and parse the repsonse

### Exercise 2 - Pytest
Goal: write a few tests

### Exercise 3 - Api client
Goal: add abstraction layer to avoid code duplication

### Exercise 4 - Fixtures
Goal: add fixtures for easy setup/teardown of tests

### Exercise 5 - Logging
Goal: add logging to find out why tests failed 


## Extras

### Extending the framework / my own framework
- jsonvalidation
- Pytest-logfest (inc. disclaimer)
- Pytest-apithon (publish first, inc. disclaimer OR explain the hook in requests)

### More Pytest
- pytest Quick Start Guide - Bruno Oliveira https://www.packtpub.com/web-development/pytest-quick-start-guide
- Python Testing with pytest: Simple, Rapid, Effective, and Scalable - Brian Okken

### More Python
- Python koans: https://github.com/gregmalcolm/python_koans
- Python Crash Course https://ehmatthes.github.io/pcc/index.html
- Hitchhiker Python book
- Raymond Hettinger - Transforming Code into Beautiful, Idiomatic Python https://www.youtube.com/watch?v=OSGv2VnC0go
- James Powell - So you want to be a Python expert? https://www.youtube.com/watch?v=cKPlPJyQrt4

### Other testing frameworks
- Tavern
- Behave: `behave` to run
- Robot framework with robotframework-requests




# My notes
- `gunicorn --reload api_app.src.app`

## ToDo list
- General explanation
- Explanation for each exercise
- Evaluate Python cheat sheet
- Expand Resources
- Next steps


## Acknowledgements
- Mark Winteringham (@1bittester): restful-booker as inspiration (https://github.com/mwinteringham/restful-booker)
- Eric Matthes for the Python Crash Course materials cheatsheet from the Python Crash Course (https://ehmatthes.github.io/pcc/cheatsheets/README.html)
- Everyone contributing to pytest, requests, falcon
