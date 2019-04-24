import pytest
from src.countWeeksBetweenMonths import solution

def test_case1():
    assert solution(2019, 1, 2, 2) == 9

def test_case2():
    assert solution(2019, 2, 4, 2) == 14

def test_case3():
    assert solution(2018, 4, 10, 1) == 31

def test_case4():
    assert solution(2018, 4, 7, 1) == 18