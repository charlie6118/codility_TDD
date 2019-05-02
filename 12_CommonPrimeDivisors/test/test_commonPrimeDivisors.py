import pytest
from src.commonPrimeDivisors import solution, gcd

def test_gcd1():
    assert gcd(24, 18) == 6

def test_gcd2():
    assert gcd(9, 5) == 1
    
def test_gcd3():
    assert gcd(10, 30) == 10

def test_case():
    assert solution([15, 10, 3], [75, 30, 5]) == 1