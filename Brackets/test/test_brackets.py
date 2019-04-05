import pytest
from src.brackets import solution

def test_string():
    assert 'a' in 'Aabced'

def test_case1():
    assert solution('(U)') == 1
    
def test_case2():
    assert solution('[U]') == 1

def test_case3():
    assert solution('{U}') == 1

def test_case4():
    assert solution('VW') == 1

def test_case5():
    assert solution('{[()()]}') == 1

def test_case6():
    assert solution('([)()]') == 0