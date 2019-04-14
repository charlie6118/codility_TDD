import pytest
from src.countSemiprimes import solution, arrayF, sieve, factorization

def test_case_sieve():
    assert sieve(17) == [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True]

# def test_case_sieve_nums():
#     assert sieveNums(17) == [2, 3, 5, 7, 11, 13, 17]

# def test_get_range():
#     assert getRange([1, 4, 16], [26, 10, 20]) == [(1, 26), (4, 10), (16, 20)]

# def test_getSemiprimes():
#     assert getSemiprimes(26, [1, 4, 16], [26, 10, 20]) == [4, 6, 9, 10, 14, 15, 21, 22, 25, 26]

def test_abs():
    assert round(26 ** 0.5) == 5

def test_max_list():
    assert max([3, 6, 11]) == 11

def test_case1():
    assert solution(26, [1, 4, 16], [26, 10, 20]) == [10, 4, 0]

def test_set():
    s = set()
    s.add(3)
    s.add(2)
    s.add(7)
    s.add(1)
    assert s == set([1, 2, 3, 7])

def test_case_arrayF():
    assert arrayF(20) == [0, 0, 0, 0, 2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2]

def test_case_factorization():
    a = arrayF(20)
    assert factorization(20, a) == [2, 2, 5]