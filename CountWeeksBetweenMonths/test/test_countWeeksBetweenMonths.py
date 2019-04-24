import pytest
from src.countWeeksBetweenMonths import solution

def test_case1():
    assert solution(2019, 1, 2, 2) == 9

def test_case2():
    assert solution(2019, 2, 4, 2) == 14
