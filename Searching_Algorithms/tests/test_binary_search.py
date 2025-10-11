import pytest
from Searching_Algorithms.binary_search import binarySearch

@pytest.mark.parametrize(
    "arr_key, target, expected",
    [
        ("basic", 10, 3),
        ("basic", 2, 0),
        ("basic", 40, 4),
        ("basic", 99, -1),
        ("empty", 1, -1),
        ("single", 5, 0),
        ("single", 1, -1),
        ("duplicates", 2, [1, 2, 3]),
        ("negatives", -5, 1),
        ("strings", "cherry", 2),
        ("long", 13, 6),
    ],
)
def test_binary_search(binary_search_arrays, arr_key, target, expected):
    arr = binary_search_arrays[arr_key]
    result = binarySearch(arr, target)
    if isinstance(expected, list):
        assert result in expected
    else:
        assert result == expected
