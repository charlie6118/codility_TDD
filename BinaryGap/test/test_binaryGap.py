import pytest
from src.binaryGap import solution

def test_decimal2binary9():
    assert '{:b}'.format(9) == '1001'

def test_decimal2binary15():
    assert '{:b}'.format(15) == '1111'

def test_decimal2binary20():
    assert '{:b}'.format(20) == '10100'

def test_decimal2binary1041():
    assert '{:b}'.format(1041) == '10000010001'

def test_decimal2binary32():
    assert '{:b}'.format(32) == '100000'

def test_binaryGap9():
    assert solution(9) == 2

def test_binaryGap15():
    assert solution(15) == 0

def test_binaryGap20():
    assert solution(20) == 1
    
def test_binaryGap1041():
    assert solution(1041) == 5

def test_binaryGap32():
    assert solution(32) == 0

def test_binaryGap6():
    assert solution(6) == 0

def test_binaryGap328():
    assert solution(328) == 2

def test_binaryGap51712():
    assert solution(51712) == 2
    