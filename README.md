# API app

## Notes

### Running app
- `gunicorn --reload api_app.app` (linux, mac)
- `waitress-serve --port=8000 api_app:app` (win)

### Simple testing
- `http localhost:8000/books`
- `http --json POST localhost:8000/books foo=bar`

### Behave tests
- `behave` to run


## ToDo list
### App
- validation on books/{id}
- authentication
- delete with authentication
- put with authentication

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