import pytest
import source.functions as my_functions


def test_add():
    res = my_functions.add(1,2)
    assert  res == 3


