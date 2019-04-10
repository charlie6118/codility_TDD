import pytest
from src.flags import solution

def test_case1():
    assert solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3

def test_case2():
    assert solution([0, 0, 0, 0, 0, 1, 0, 1, 0, 1]) == 2

def test_case3():
    assert solution([1, 3, 2]) == 1