import pytest
import array as arr
from src.cyclicRotation import solution

def test_arrayDef():
    assert str(type(arr.array('b', [3, 8, 9, 7]))) == '<class \'array.array\'>'

def test_rotate1():
    assert solution(arr.array('b', [3, 8, 9, 7, 6]), 1) == arr.array('b', [6, 3, 8, 9, 7])

def test_rotate3():
    assert solution(arr.array('b', [3, 8, 9, 7, 6]), 3) == arr.array('b', [9, 7, 6, 3, 8])

def test_array000rotate1():
    assert solution(arr.array('b', [0, 0, 0]), 1) == arr.array('b', [0, 0, 0])

def test_array1234rotate4():
    assert solution(arr.array('b', [1, 2, 3, 4]), 4) == arr.array('b', [1, 2, 3, 4])

def test_emptyArray():
    assert solution(arr.array('b', []), 4) == arr.array('b', [])
