import pytest
from src.maxNonoverlappingSegments import solution

def test_case1():
    assert solution([], []) == 0

def test_case2():
    assert solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]) == 3

def test_case3():
    assert solution([], []) == 0