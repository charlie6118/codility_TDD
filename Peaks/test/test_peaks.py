import pytest
from src.peaks import *

def test_case1():
    assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3