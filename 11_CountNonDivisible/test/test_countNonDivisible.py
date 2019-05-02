import pytest
from src.countNonDivisible import solution

def test_case1():
    assert solution([3, 1, 2, 3, 6]) == [2, 4, 3, 2, 0]

def test_dictionary():
    dic = {}
    dic[3] = 4
    dic[6] = 0
    print(dic)
    assert dic.get(3) == 4
    assert not dic.get(5)
