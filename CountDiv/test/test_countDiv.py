import pytest
from src.countDiv import solution

def test_list_loop():
    assert [n for n in range(6, 12)] == [6, 7, 8, 9, 10, 11]

def test_sample():
    assert solution(6, 11, 2) == 3

def test_extreme():
    assert solution(0, 2000000000, 1) == 2000000001
