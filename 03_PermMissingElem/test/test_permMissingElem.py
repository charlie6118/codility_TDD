import pytest
import array as arr
from src.permMissingElem import solution
from src.permMissingElem import bubbleSort

def test_bubbleSort():
    assert bubbleSort(arr.array('b', [2, 3, 1, 5])) == arr.array('b', [1, 2, 3, 5])

def test_sample1():
    assert solution(arr.array('b', [2, 3, 1, 5])) == 4

def test_sample2():
    assert solution(arr.array('b', [2, 3, 1, 5, 4, 9, 8, 7])) == 6

def test_sampleSingleElement():
    assert solution(arr.array('b', [1])) == 2

def test_sampleMissingFirst():
    assert solution(arr.array('b', [2, 3, 4, 5])) == 1

def test_sampleMissingLast():
    assert solution(arr.array('b', [2, 3, 1])) == 4