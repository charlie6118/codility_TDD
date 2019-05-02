import pytest
import array as arr
from src.tapeEquilibrium import solution

def test_sample1():
    assert solution(arr.array('b', [3, 1, 2, 4, 3])) == 1

def test_twoElement():
    assert solution(arr.array('h', [-1000, 1000])) == 2000
