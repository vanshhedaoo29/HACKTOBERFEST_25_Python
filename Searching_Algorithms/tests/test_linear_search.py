import pytest
from Searching_Algorithms.linear_search import linearSearch

@pytest.mark.parametrize(
    "arr_key, target, expected",
    [
        ("basic", 3, 2),
        ("mixed", 5, 4),
        ("not_found", 6, -1),
        ("empty", 1, -1),
        ("single_match", 1, 0),
        ("single_miss", 1, -1),
        ("duplicates", 2, 1),
        ("first", 5, 0),
        ("last", 4, 3),
        ("negatives", -5, 1),
        ("strings", "banana", 1),
        ("mixed_types", "two", 1),
    ],
)
def test_linear_search(linear_search_arrays, arr_key, target, expected):
    arr = linear_search_arrays[arr_key]
    result = linearSearch(arr, target)
    assert result == expected
