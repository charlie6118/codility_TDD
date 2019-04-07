import pytest
from src.stoneWall import solution


def test_array_behavior():
    sample = [8, 8, 5, 7, 9, 8, 7, 4, 8, 4, 4]
    minA = min(sample)
    i = sample.index(minA)
    assert True

def test_case1():
    assert solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7