import pytest
from src.oddOccurrencesInArray import solution
import array as arr

def test_arrayDef():
    assert str(type(arr.array('b', [3, 8, 9, 7]))) == '<class \'array.array\'>'

def test_testcaseSingleItem():
    assert solution(arr.array('b', [9])) == 9

def test_testcase1():
    assert solution(arr.array('b', [9, 3, 9, 3, 9, 7, 9])) == 7

def test_creatDict():
    thisDict = {
        9: 1,
        3: 2
    }
    assert thisDict[3] == 2