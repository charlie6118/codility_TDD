import pytest
from src.maxProfit import solution

def test_list_behavior():
    temp = [3, 2, 1, 5, 6]
    assert temp[1:len(temp)] == [2, 1, 5, 6]

def test_case1():
    assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356

def test_case_empty():
    assert solution([]) == 0