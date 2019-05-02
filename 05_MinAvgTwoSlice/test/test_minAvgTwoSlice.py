import pytest
from src.minAvgTwoSlice import solution

def test_sample1():
    assert solution([4, 2, 2, 5, 1, 5, 8]) == 1

def test_sample2():
    assert solution([10000, -10000]) == 0

def test_sample3():
    assert solution([-3, -5, -8, -4, -10]) == 2
