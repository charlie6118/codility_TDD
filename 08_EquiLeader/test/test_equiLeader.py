import pytest
from src.equiLeader import solution

def test_case1():
    assert solution([4, 3, 4, 4, 4, 2]) == 2

def test_case2():
    assert solution([3]) == 0

def test_case4():
    assert solution([3, 2]) == 0

def test_case5():
    assert solution([3, 3]) == 1

def test_case6():
    assert solution([1, 3, 3]) == 0

def test_case7():
    assert solution([0, 0] ) == 1