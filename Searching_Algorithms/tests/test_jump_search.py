import pytest
from Searching_Algorithms.jump_search import jumpSearch

def test_jump_search_basic(jump_search_basic_cases):
    for arr, target, expected in jump_search_basic_cases:
        assert jumpSearch(arr, target, len(arr)) == expected

def test_jump_search_duplicates(jump_search_duplicates_array):
    arr = jump_search_duplicates_array
    result = jumpSearch(arr, 2, len(arr))
    assert result in [1, 2, 3]

def test_jump_search_various_types(jump_search_various_types):
    for arr, target, expected in jump_search_various_types:
        assert jumpSearch(arr, target, len(arr)) == expected

def test_final_return_with_block_boundary(jump_search_block_boundary):
    arr = jump_search_block_boundary
    target = 8
    assert jumpSearch(arr, target, len(arr)) == -1

def test_step_zero_condition(monkeypatch):
    import Searching_Algorithms.jump_search as jump_search_module
    monkeypatch.setattr(jump_search_module.math, "sqrt", lambda n: 0)
    result = jump_search_module.jumpSearch([1, 2, 3], 2, 3)
    assert result == 1
