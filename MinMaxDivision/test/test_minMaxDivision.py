import pytest
from src.minMaxDivision import *

def test_case1():
    assert solution(3, 5, [2, 1, 5, 1, 2, 2, 2]) == 6

def test_case2():
    assert solution(10, 5, [2, 1, 5, 1, 2, 2, 2]) == 5

def test_case3():
    assert solution(1, 5, [2, 1, 5, 1, 2, 2, 2]) == 15

def test_case4():
    assert solution(4, 10, [3, 4, 5, 6, 7, 8]) == 11