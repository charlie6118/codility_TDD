import pytest
import array as arr
from src.maxCounters import solution

def test_first():
    assert solution(5, arr.array('b', [3, 4, 4, 6, 1, 4, 4])) == [3, 2, 2, 4, 2]