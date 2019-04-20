import pytest
from src.nailingPlanks import *

def test_case1():
    A = [1, 4, 5, 8]
    B = [4, 5, 9, 10]
    C = [4, 6, 7, 10, 2]
    assert solution(A, B, C) == 4

def test_case2():
    assert solution([2], [2], [1]) == -1