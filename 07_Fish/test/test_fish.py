import pytest
from src.fish import solution

def test_list_pop():
    l = [4, 2]
    assert l.pop() == 2

def test_list_append():
    l = [4, 2]
    l.append(3)
    assert l == [4, 2, 3]

def test_case1():
    assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2

def test_case2():
    assert solution([1], [0]) == 1