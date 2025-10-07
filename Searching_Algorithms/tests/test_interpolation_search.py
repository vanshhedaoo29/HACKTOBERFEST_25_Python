import pytest
from Searching_Algorithms.interpolation_search import interpolationSearch

@pytest.mark.parametrize(
    "arr_key, target, expected",
    [
        ("basic", 18, 4),       # middle
        ("basic", 10, 0),       # first element
        ("basic", 47, 14),      # last element
        ("basic", 99, -1),      # not found
        ("empty", 1, -1),       # empty array
        ("single", 7, 0),       # single-element match
        ("single", 5, -1),      # single-element miss
        ("small", 15, 2),       # small array
        ("not_found", 11, -1),  # element not present
        ("duplicates", 10, 0),  # first occurrence of 10
        ("duplicates", 13, 2),  # first occurrence of 13
        ("all_equal", 5, 0),    # all elements same, target found
        ("all_equal", 7, -1),   # all elements same, target not found
        ("negatives", -10, 1),  # negative values
        ("negatives", 30, -1),  # negative array, target not present
    ]
)
def test_interpolation_search(arr_key, target, expected, interpolation_search_arrays):
    arr = interpolation_search_arrays[arr_key]
    n = len(arr)
    result = interpolationSearch(arr, n, target)
    assert result == expected

@pytest.mark.parametrize(
    "arr, target, expected",
    [
        # Edge cases for type errors / unsupported inputs
        (["a", "b", "c", "d"], "c", -1),
        ([], "a", -1),
        ([1, 2, 3], "2", -1),
        ([5, 5, 5, 5], 7, -1),  # all equal, target not found
        ([7], 10, -1),          # single element, target not found
    ],
)
def test_interpolation_search_edge_cases(arr, target, expected):
    n = len(arr)
    assert interpolationSearch(arr, n, target) == expected
