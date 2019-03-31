import pytest
import array as arr
from src.frogRiverOne import solution

def test_one():
    assert solution(5, arr.array('b', [1, 3, 1, 4, 2, 3, 5, 4])) == 6


