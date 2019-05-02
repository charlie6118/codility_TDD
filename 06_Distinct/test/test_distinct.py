import pytest
from src.distinct import solution

def test_case1():
    assert solution([2, 1, 1, 2, 3, 1]) == 3
    
def test_case2():
    assert solution([]) == 0
    
def test_case3():
    assert solution([-1000000, 1000000]) == 2
    