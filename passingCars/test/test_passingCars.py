import pytest
from src.passingCars import solution
from array import array

def test_testCase1():
    assert solution(array('b', [0, 1, 0, 1, 1])) == 5

def test_testCase2():
    assert solution(array('b', [0, 0, 1, 0, 0])) == 2

def test_testCase3():
    assert solution(array('b', [1, 0, 0, 0, 1])) == 3
