import pytest
from src.maxDoubleSliceSum import solution

def test_case1():
    assert solution([3, 2, 6, -1, 4, 5, -1, 2]) == 17

def test_case_three_input():
    assert solution([3, 2, 1]) == 0