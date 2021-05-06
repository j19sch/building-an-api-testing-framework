# Debugging

Sometimes test results and logging are not enough to determine why tests are misbehaving. Is there a problem with
the test, the framework, the product, or a combination of these three? This is where debugging shines.
It allows you to walk through the code line-by-line, observing what it does as it runs.


## Debugging with pytest

### On failures
With `pytest --pdb` you can drop into the debugger on every failure.
More info here: https://docs.pytest.org/en/latest/usage.html#dropping-to-pdb-python-debugger-on-failures

### At the start of a test
With `pytest --trace` you can drop into the debugger at the start of each test.
More info here: https://docs.pytest.org/en/latest/usage.html#dropping-to-pdb-python-debugger-at-the-start-of-a-test


### pdb - The Python Debugger
The out-of-the-box Python debugger, very bare bones.

More info:
- https://docs.python.org/2.7/library/pdb.html
- https://docs.python.org/3/library/pdb.html

Some basic `pdb` commands:
- `help` - shows available commands
- `help <command>` - shows help text of command
- `l`, `list` - lists source code (11 lines around current line)
- `n`, `next` - continue execution until the next line in the current function is reached or it returns.
- `s`, `step` - execute the current line, stop at the first possible occasion (either in a function that is called or in the current function).
- `c`, `cont` - continue execution until breakpoint or until all code has been executed
- `a`, `args` - print the argument list of the current function.
- `p <variable name>` - print value of variable
- `whatis <variable name>` - print type of variable

The difference between `next` and `step`, is that with `next` you will remain on the same level in the code. So if you are debugging your test with `--trace`, `pdb` will stop at every line in that test, but not go deeper. If you want to delve into functions and methods called from your test, `step` allows you to step into these functions and methods. If you want to go one lever deeper still, use `step` again.


## Other debugging tools

### pdb++
A drop-in replacement for `pdb` with some usability improvements.

More info: https://github.com/antocuni/pdb


### pudb
A full-screen, console-based visual debugger.

More info: https://github.com/inducer/pudb


### PyCharm
The PyCharm IDE supports pytest, allowing you to run and debug tests from the IDE itself.

More info: https://www.jetbrains.com/help/pycharm/pytest.html


### Visual Studio Code
Visual Studio Code supports pytest, allowing you to run and debug tests from the IDE itself.

More info: https://code.visualstudio.com/docs/python/testing#_debug-tests
