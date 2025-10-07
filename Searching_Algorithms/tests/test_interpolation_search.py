import pytest
from Searching_Algorithms.interpolation_search import interpolationSearch

@pytest.mark.parametrize(
    "arr_key, target, expected",
    [
        ("basic", 18, 4),      # middle
        ("basic", 10, 0),      # first element
        ("basic", 47, 14),     # last element
        ("basic", 99, -1),     # not found
        ("empty", 1, -1),      # empty array
        ("single", 7, 0),      # single element match
        ("single", 5, -1),     # single element miss
        ("small", 15, 2),      # small array
        ("not_found", 11, -1), # missing element
        ("duplicates", 10, [0, 3]), # duplicates, any valid index
        ("duplicates", 13, [2, 4]), # duplicates, any valid index
    ]
)
def test_interpolation_search(interpolation_search_arrays, arr_key, target, expected):
    arr = interpolation_search_arrays[arr_key]
    n = len(arr)
    result = interpolationSearch(arr, n, target)
    if isinstance(expected, list):
        assert result in expected
    else:
        assert result == expected


def test_interpolation_single_element_edge(interpolation_search_arrays):
    """Cover low==high branch for single-element arrays."""
    arr = [42]
    n = len(arr)
    
    # Match case
    assert interpolationSearch(arr, n, 42) == 0
    # No match case
    assert interpolationSearch(arr, n, 7) == -1


def test_interpolation_same_low_high_edge():
    """Cover division when arr[high] == arr[low] and x != arr[low]."""
    arr = [5, 5, 5]
    n = len(arr)
    # Searching for something not in array
    assert interpolationSearch(arr, n, 3) == -1
