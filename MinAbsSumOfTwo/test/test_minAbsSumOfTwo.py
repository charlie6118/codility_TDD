import pytest
from src.minAbsSumOfTwo import solution

def test_case1():
    assert solution([1, 4, -3]) == 1

def test_case2():
    assert solution([-8, 4, 5, -10, 3]) == 3


