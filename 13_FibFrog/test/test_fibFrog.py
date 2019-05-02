import pytest
from src.fibFrog import *

def test_case1():
    A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
    assert solution(A) == 3

def test_case2():
    A = [0, 0, 0]
    assert solution(A) == -1

# def test_leaves():
#     A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
#     assert countLeaves(A) == [4, 5, 7, 12]
