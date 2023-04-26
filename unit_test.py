import pytest

def multiply(x, y):
    return x*y


def test_multiply():
    assert multiply(10, 2) == 20


