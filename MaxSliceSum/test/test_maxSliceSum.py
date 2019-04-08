import pytest
from src.maxSliceSum import solution

def test_list_behavior():
    temp = [3, 2, 1, 5, 6]
    assert temp[1:len(temp)] == [2, 1, 5, 6]

def test_case1():
    assert solution([3, 2, -6, 4, 0]) == 5

def test_case_empty():
    assert solution([-10]) == -10