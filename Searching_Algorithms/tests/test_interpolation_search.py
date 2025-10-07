import pytest
from Searching_Algorithms.interpolation_search import interpolationSearch

# ----------------------------
# PARAMETRIZED SEARCH TESTS
# ----------------------------

@pytest.mark.parametrize(
    "arr_key, target, expected",
    [
        ("basic", 18, 4),
        ("basic", 10, 0),
        ("basic", 47, 14),
        ("basic", 99, -1),          # not found
        ("empty", 1, -1),            # empty array
        ("single", 7, 0),            # single-element match
        ("single", 5, -1),           # single-element miss
        ("small", 15, 2),            # small array
        ("not_found", 11, -1),       # element not present
        ("duplicates", 10, 2),       # first occurrence of 10
        ("duplicates", 13, 4),       # first occurrence of 13
        ("all_equal", 5, 0),         # all elements same, target found
        ("all_equal", 7, -1),        # all elements same, target not found
        ("negatives", -10, 1),       # negative values
        ("negatives", 30, -1),       # negative array, target not present
    ]
)
def test_interpolation_search(arr_key, target, expected, interpolation_search_arrays):
    arr = interpolation_search_arrays[arr_key]
    n = len(arr)
    result = interpolationSearch(arr, n, target)
    assert result == expected

# ----------------------------
# TEST UNSUPPORTED TYPES
# ----------------------------

@pytest.mark.parametrize(
    "arr",
    [
        "strings",
        "mixed_types",
    ]
)
def test_interpolation_search_unsupported_types(arr, interpolation_search_arrays):
    """Interpolation search should return -1 for non-numeric arrays."""
    array = interpolation_search_arrays[arr]
    n = len(array)
    result = interpolationSearch(array, n, 0)
    assert result == -1
