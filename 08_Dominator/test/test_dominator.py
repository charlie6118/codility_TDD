import pytest
from src.dominator import solution

def test_stack_behavior():
    stack = [3, 4, 3, 2, 3, -1, 3]
    assert stack[-1] == 3
    assert stack[-2] == -1

def test_case1():
    assert solution([3, 4, 3, 2, 3, -1, 3, 3]) == 0

def test_case2():
    assert solution([3]) == 0

def test_case3():
    assert solution([]) == -1

def test_case4():
    assert solution([3, 2]) == -1

def test_case5():
    assert solution([3, 3]) == 0

def test_case6():
    assert solution([1, 3, 3]) == 1