"""Testing module to check functionalities of pytest"""

# test Isort : import ordering on save

from __future__ import nested_scopes

import pytest

# test black
l = (
    ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
    + ["LongString"]
)


# Test pylint disable
# pylint: disable=W0613
def test_black_args(*args):
    """dummy test"""


# Testing arguments reorgani
test_black_args(
    "LongString",
    "LongString",
    "LongString",
    "LongString",
    "LongString",
    "LongString",
    "LongString",
)
test_black_args(
    "LongString", "LongString", "LongString", "LongString", "LongString", "LongString"
)

# There shoud be a type error from mypy
a: int = "abc"


@pytest.fixture
def mylist():
    return [1, 2, 3]


@pytest.mark.skip
def test_a1():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1


@pytest.mark.parametrize("a", [1, 20, 300])
@pytest.mark.parametrize("b", [1000, 2000, 3000])
def test_parametrize(a, b):
    assert a < b


def test_list(mylist):
    assert len(mylist) == 3
