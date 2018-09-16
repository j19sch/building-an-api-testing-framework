# API app

Important: this app is intended as a practice app for a testing workshop, so I took some shortcuts. ;-)

## Notes

### Running app
- `gunicorn --reload api_app.app` (linux, mac)
- `waitress-serve --port=8000 api_app:app` (win)

### Simple testing
- `http -v localhost:8000/books`
- `http -v --json POST localhost:8000/books foo=bar`

### Behave tests
- `behave` to run


## ToDo list
### App
- works in python 2 and python 3

### Exercises
- keep up-to-date wrt App
- ex3
- ex4
- ex5


### Other
- General explanation
- Explanation for each exercise
- Python cheat sheet
- Resources
- Next steps