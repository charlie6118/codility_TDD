import pytest
from src.genomicRangeQuery import solution
from array import array

def test_sample():
    assert solution('CAGCCTA', [2, 5, 0], [4, 5, 6]) == [2, 4, 1]

def test_Faliure():
    assert solution('TC', [0, 0, 1], [0, 1, 1]) == [4, 2, 2]