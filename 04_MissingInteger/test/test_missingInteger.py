import pytest
from array import array
from src.missingInteger import solution

def test_case1():
    assert solution(array('b', [1, 2, 3])) == 4

def test_case2():
    assert solution(array('b', [-1, -3])) == 1

def test_case3():
    assert solution(array('b', [1, 3, 6, 4, 1, 2])) == 5