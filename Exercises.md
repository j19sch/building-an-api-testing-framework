# Exercises

Below are the descriptions of the exerises, including the learning goal.  

Example solutions can be found in the `example_solutions` directory.  

Note that different solutions are possible.
As your framework and tests grow, you will probably move from one solution to a different one. The example
solutions have been created to most clearly illustrate the purpose of the exercise.  

Also note that because of the limited scope of the exercises, the solutions seem over-elaborate.


## General info
- running the app
- restarting the app



## Exercise 1 - requests library
**Goal**: become familiar with the requests library

### Assignment
Print the status code and response for the following API calls:
- GET knockknock
- GET books
- GET one book
- POST a book
- POST auth

### info
- get
- post json()
- response, response.status_code, response.text, response.json()



## Exercise 2 - pytest
**Goal**: become familiar with pytest

### Assignment
Build tests for the API calls of exercise 1.

### Info
- `test_`
- `pytest` or `pytest <filename>`



## Exercise 3 - API client
**Goal**: build an interface between the API and your tests

### Assignment
Create an API client module as an abstraction layer between the API and your tests.  
You can use classes if you want to, but you don't need to.

Make sure you see the following:
- passing test
- failing test
- erroring test



## Exercise 4 - fixtures
**Goal**: use fixtures for test setup and teardown

### Assignment
Create a test using fixtures in which you:
- get a token
- create a book
- delete that book

### Info
- fixtures


## Exercise 5 - logging

**Goal**: add logging so allow you to debug more easily

### Assignment
Add logging to your tests by using the requests hook.

### Info
- logging