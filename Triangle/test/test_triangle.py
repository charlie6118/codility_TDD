import pytest
from src.triangle import solution

def test_case_T1():
    assert solution([10, 2, 5, 1, 8, 20]) == 1

def test_case_F1():
    assert solution([10, 50, 5, 1]) == 0

def test_case_F2():
    assert solution([10, 50]) == 0