import pytest
from Searching_Algorithms.fibonacci_search import fibonacciSearch

@pytest.mark.parametrize(
    "arr_key, target, expected",
    [
        ("basic", 10, 3),
        ("basic", 2, 0),
        ("basic", 40, 4),
        ("not_found", 11, -1),
        ("empty", 1, -1),
        ("single_match", 5, 0),
        ("single_miss", 5, -1),
        ("long", 85, 8),
        ("negatives", -10, 1),
        ("strings", "cherry", 2),
    ],
)
def test_fibonacci_search(fibonacci_search_arrays, arr_key, target, expected):
    arr = fibonacci_search_arrays[arr_key]
    result = fibonacciSearch(arr, target)
    assert result == expected
