
import pytest
import func

def test_add():
    expected_result = 3
    addition_result = func.add(1, 2)
    assert addition_result == expected_result

def test_my_abs():
    expected_result = 0
    absolute_result = func.my_abs(0)
    assert absolute_result == expected_result
