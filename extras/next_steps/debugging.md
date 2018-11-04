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


## Debugging tools

### pdb - The Python Debugger
The out-of-the-box Python debugger, very bare bones.

More info:
- https://docs.python.org/2.7/library/pdb.html
- https://docs.python.org/3/library/pdb.html


### pdb++
A drop-in replacement for `pdb` with some usability improvements.

More info: https://github.com/antocuni/pdb


### pudb
A full-screen, console-based visual debugger.

More info: https://github.com/inducer/pudb


### PyCharm
The PyCharm IDE supports pytest, allowing you to run and debug tests from the IDE itself.

More info: https://www.jetbrains.com/help/pycharm/pytest.html
