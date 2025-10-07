import pytest
from Searching_Algorithms.jump_search import jumpSearch


# --- BASIC / EDGE / NOT FOUND CASES ---
@pytest.mark.parametrize(
    "arr_key, target, expected",
    [
        ("basic", 3, 2),                  # middle
        ("basic", 1, 0),                  # first
        ("basic", 5, 4),                  # last
        ("between_values", 4, -1),        # target between values
        ("beyond_end", 4, -1),            # target beyond end
        ("empty", 1, -1),                 # empty array
        ("single_match", 5, 0),           # single element found
        ("single_miss", 3, -1),           # single element not found
        ("smaller_than_first", 5, -1),    # target smaller than first element
        ("final_return_block", 3, -1),    # triggers final return
    ],
)
def test_jump_search_basic(jump_search_arrays, arr_key, target, expected):
    """Test jump search with basic, edge, and final return cases."""
    arr = jump_search_arrays[arr_key]
    n = len(arr)
    assert jumpSearch(arr, target, n) == expected


# --- DUPLICATES ---
@pytest.mark.parametrize(
    "arr_key, target, valid_indices",
    [
        ("duplicates", 2, [1, 2, 3]),
    ],
)
def test_jump_search_duplicates(jump_search_arrays, arr_key, target, valid_indices):
    """Test jump search with duplicate elements."""
    arr = jump_search_arrays[arr_key]
    result = jumpSearch(arr, target, len(arr))
    assert result in valid_indices


# --- DIFFERENT DATA TYPES ---
@pytest.mark.parametrize(
    "arr_key, target, expected",
    [
        ("various_types_int", 2, 1),
        ("various_types_float", 2.5, 1),
        ("various_types_str", "b", 1),
    ],
)
def test_jump_search_various_types(jump_search_arrays, arr_key, target, expected):
    """Test ints, floats, and strings."""
    arr = jump_search_arrays[arr_key]
    assert jumpSearch(arr, target, len(arr)) == expected


# --- FINAL RETURN WITH BLOCK BOUNDARIES ---
def test_final_return_with_block_boundary(jump_search_arrays):
    """Hit final return when target is missing in a middle block."""
    arr = jump_search_arrays["block_boundary"]
    target = 8
    result = jumpSearch(arr, target, len(arr))
    assert result == -1


# --- STEP ZERO CONDITION ---
def test_step_zero_condition(monkeypatch):
    """Test when math.sqrt(n) returns 0, forcing step = 1."""
    import Searching_Algorithms.jump_search as jump_search_module
    monkeypatch.setattr(jump_search_module.math, "sqrt", lambda n: 0)
    arr = [1, 2, 3]
    result = jump_search_module.jumpSearch(arr, 2, len(arr))
    assert result == 1
