# Live coding cheatsheet

## final checklist
- did you do all the setup?
- is everything readable from the back of the room?
- identify a problem and solve it
- makes notes and commits as you go
- narrate your thoughts, don't read your code out loud


## cheats
```
book_to_delete = {
    "author": "Ray Monk", 
    "pages": 110, 
    "publisher": "Granta Books, London", 
    "sub_title": None, 
    "title": "How to read Wittgenstein", 
    "year": 2005
}
```

`self.hooks['response'].append(self._log_stuff)`

`def _log_stuff(response, *args, **kwargs):`


## setup

### do
- create a branch, create a link, share it
- python3 venv with dependencies
- light themes and large font
	- sublime
	- terminal
- api app running
- separate folder for tests
- change prompt: `export PS1="\u:\[\033[01;34m\]\W\[\033[00m\]$(__git_ps1 " (%s)")\$ "`

### open
- cheatsheet
- API docs
- requests docs
- pytest docs


## waypoints
### step 1 - calling an API
- use library that's transparent

### step 2 - pytest
- use library that makes testing easier

### step 3 - fixtures
- separate setup/teardown from tests

### step 4 - API clients
- seperate interface code from tests

### step 5 - logging
- more transparency

### heuristic
- CRUDDER - steps - test & code
	- CRUD -> tests & code
	- Debug -> code
	- Explore -> test
	- Run & report -> code & test

### conclusion
How is your framework helping you to do better testing? (all of it!)


## timing
45 minutes in total
- 5 minutes intro
- 30 minutes of live coding
	1. calling API
	2. pytest
	3. fixtures
	4. API clients
	5. logging
- 5 minutes wrap-up
- 5 minutes Q&A