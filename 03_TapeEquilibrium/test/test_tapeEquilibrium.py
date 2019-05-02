import pytest
from src.tapeEquilibrium import solution

def test_sample1():
    assert solution([3, 1, 2, 4, 3]) == 1

def test_twoElement():
    assert solution([-1000, 1000]) == 2000

def test_sample2():
    assert solution([-10, -20, -30, -40, 100]) == 20
