import pytest
import logging
from functools import partial


# @pytest.fixture
# def failed_soft_asserts(request):
#     failed = []
#     yield failed
#
#     if len(failed) > 0:
#         print(failed)
#
#
#
# def test_with_soft_assert(failed_soft_asserts):
#     try:
#         assert False
#     except AssertionError:
#         failed_soft_asserts.append("Some soft assert failed")


@pytest.fixture
def soft_assert(request):

    failed_asserts = []

    def _soft_assert(expr, fail_list=failed_asserts):
        try:
            assert expr
        except AssertionError as e:
            failed_asserts.append("oops")
            logging.error(e)

    _soft_assert_funct = partial(_soft_assert, fail_list=failed_asserts)

    yield _soft_assert_funct

    if len(failed_asserts) > 0:
        request._failed_soft_asserts = failed_asserts
        logging.error(failed_asserts)


def test_failing_test(soft_assert):
    soft_assert(1 == 2)
    soft_assert(3 == 4)
