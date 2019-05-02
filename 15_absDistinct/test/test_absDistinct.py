import pytest
from src.absDistinct import *

def test_case1():
    assert solution([-5, -3, -1, 0, 3, 6]) == 5
    
def test_case2():
    assert solution([-10]) == 1

def test_case3():
    assert solution([-2, 1]) == 2

def test_case4():
    assert solution([-2147483648, 0]) == 2