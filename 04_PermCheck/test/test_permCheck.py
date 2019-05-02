import pytest
from src.permCheck import solution

def test_simpleTrue():
    assert solution([4, 1, 3, 2]) == 1

def test_simpleFalse():
    assert solution([4, 1, 3]) == 0

def test_totalSumCorrectButNotPermutation():
    assert solution([3, 0, 3]) == 0