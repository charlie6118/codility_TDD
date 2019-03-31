import pytest
import array as arr
from src.permCheck import solution

def test_simpleTrue():
    assert solution(arr.array('b', [4, 1, 3, 2])) == 1

def test_simpleFalse():
    assert solution(arr.array('b', [4, 1, 3])) == 0

def test_totalSumCorrectButNotPermutation():
    assert solution(arr.array('b', [3, 0, 3])) == 0