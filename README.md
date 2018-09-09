# API app

## Running app
- `gunicorn --reload api_app.app` (linux, mac)
- `waitress-serve --port=8000 api_app:app` (win)

## Simple testing
- `http localhost:8000/books`
- `http --json POST localhost:8000/books foo=bar`

## Behave tests