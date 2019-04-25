import pytest
from src.numberSolitaire import *

def test_case1():
    assert solution([1, -2, 0, 9, -1, -2]) == 8

def test_case2():
    assert solution([-2, 5, 1]) == 4