import pytest
import math
from src.ladder import *

def test_fab():
    assert fab(5) == 5

def test_modulo():
    assert 5 % pow(2, 3) == 5
    assert 5 % pow(2, 2) == 1
    assert 8 % pow(2, 4) == 8
    assert 8 % pow(2, 3) == 0
    assert 1 % pow(2, 1) == 1

def test_case():
    # assert solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]) == [5, 5, 8, 8, 1]
    assert solution([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]) == [5, 1, 8, 0, 1]