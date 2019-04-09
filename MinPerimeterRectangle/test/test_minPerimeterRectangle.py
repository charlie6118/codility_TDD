import pytest
from src.minPerimeterRectangle import solution

def test_case1():
    assert solution(30) == 22

def test_case2():
    assert solution(36) == 24