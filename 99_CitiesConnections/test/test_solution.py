import pytest
from src.solution import *

def test_case_findCapital():
    assert findCapital([9, 1, 4, 9, 0, 4, 8, 9, 0, 1]) == 1

def test_case_how_many_children_cities_connected_to_parent_city():
    assert citiesConnections([9, 1, 4, 9, 0, 4, 8, 9, 0, 1]) == {0: [4, 8], 1: [9], 4: [2, 5], 8: [6], 9: [0, 3, 7]}

def test_case_mark_layers():
    assert markLayers({0: [4, 8], 1: [9], 4: [2, 5], 8: [6], 9: [0, 3, 7]}, 1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0) == [2, 0, 4, 2, 3, 4, 4, 2, 3, 1]

def test_case_sample():
    assert solution([9, 1, 4, 9, 0, 4, 8, 9, 0, 1]) == [1, 3, 2, 3, 0, 0, 0, 0, 0]

def test_case_empth():
    assert solution([]) == []

def test_case_one_element():
    assert solution([0]) == []