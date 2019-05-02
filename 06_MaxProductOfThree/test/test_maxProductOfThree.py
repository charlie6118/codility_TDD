import pytest
from src.maxProductOfThree import solution

def test_case1():
    assert solution([-3, 1, 2, -2, 5, 6]) == 60

def test_case_no_plus():
    assert solution([-3, -4, -1, -9]) == -12

def test_case_no_minus():
    assert solution([3, 4, 1, 9]) == 108

def test_case_no_bound():
    assert solution([-1000, 1000, -1]) == 1000000

def test_case_simple1():
    assert solution([-2, -3, -5, -6, 0]) == 0
