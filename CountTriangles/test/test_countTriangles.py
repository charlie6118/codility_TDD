import pytest
from src.countTriangles import *

def test_case1():
    assert solution([10, 2, 5, 1, 8, 12]) == 4

def test_case2():
    assert solution([5, 5, 3]) == 1