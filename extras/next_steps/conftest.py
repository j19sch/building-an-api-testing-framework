import pytest

# https://stackoverflow.com/questions/10754970/in-which-py-test-callout-can-i-find-both-item-and-report-data
# https://docs.pytest.org/en/latest/writing_plugins.html#hookwrapper-executing-around-other-hooks

# gremlins
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#
#     setattr(item, "rep_" + rep.when, rep)
#     ??? return rep


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        print(rep.__dict__)
        print(item.__dict__)
        print(call.__dict__)
        # rep.outcome = 'failed'
