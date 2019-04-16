import pytest
from src.chocolatesByNumbers import solution, gcd

def test_gcd1():
    assert gcd(24, 9) == 3

def test_gcd2():
    assert gcd(24, 18) == 6

def test_case():
    assert solution(10, 4) == 5