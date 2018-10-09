# API app

**Disclaimer**: 
This app is intended as a practice app for a testing workshop, so I took some shortcuts. ;-)


## Setup & installation

### Python and VirtualEnv
- Install Python
    - Python 2.7 is fine. If you need to install Python, take Python 3 (it's the future).
    - Instructions: https://ehmatthes.github.io/pcc/chapter_01/README.html (do not install Geany)
- Install virtualenv (`pip|pip3 install --user virtualenv`)

### Setup a virtual environment
- Create virtualenv (`virtualenv venv`)
- Activate virtualenv (linux, mac: `source venv/bin/activate`) or (win: `venv\bin\activate.bat`)

### Download and install this repo
- download this repository (download the zip file or `git clone`)
- Install requirements.txt (`pip|pip3 install -r requirements.txt`)
- Install gunicorn (linux, mac: `pip|pip3 install gunicorn`) or waitress (win: `pip|pip3 install waitress`)

## Running the app
- linux, mac: `gunicorn api_app.src.app` or win: `waitress-serve --port=8000 api_app:src:app`
- smoke test by using your browser to go to `localhost:8000/knockknock` 

## Advaced text editor
- Any advanced text editor with the following features will do:
    - syntax highlighting (easier to read)
    - word completion (avoids typos in names of variables, functions and methods)
- If you're note sure which one to use, Visual Studio Code is a good choice (https://code.visualstudio.com/)
- Using an IDE like PyCharm is fine too.


## Exercises
- see `API-docs.md` for a description of the API
- see `./exercises` for the different exercises
- check `./example_solutions` for example solutions to the exercises

### Reference materials
- Python cheatsheet https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc.pdf
- Requests: http://docs.python-requests.org/en/master/
- Pytest: https://docs.pytest.org/en/latest/contents.html and https://docs.pytest.org/en/latest/reference.html



## Extras

### Same test, different tools
Test deleting a book, implemented with:
- behave: `behave <path>`
- pytest and requests: `pytest <path>`
- robot framework with roborframework-requests: `robot <path>`
- tavern: `pytest <path>`

ToDo: create book to delete in test, instead of deleting first on of retrieved books


### next steps
- jsonvalidation
- (todo) Pytest-logfest (inc. disclaimer)

### More Pytest
- pytest Quick Start Guide - Bruno Oliveira https://www.packtpub.com/web-development/pytest-quick-start-guide
- Python Testing with pytest: Simple, Rapid, Effective, and Scalable - Brian Okken

### More Python
- Python koans: https://github.com/gregmalcolm/python_koans
- Raymond Hettinger - Transforming Code into Beautiful, Idiomatic Python https://www.youtube.com/watch?v=OSGv2VnC0go
- James Powell - So you want to be a Python expert? https://www.youtube.com/watch?v=cKPlPJyQrt4



# My notes
- `gunicorn --reload api_app.src.app`
- `kill -HUP <masterpid>`



## Acknowledgements
- Mark Winteringham (@1bittester): restful-booker as inspiration (https://github.com/mwinteringham/restful-booker)
- Eric Matthes for the Python Crash Course materials cheatsheet from the Python Crash Course (https://ehmatthes.github.io/pcc/cheatsheets/README.html)
- Everyone contributing to pytest, requests, falcon
