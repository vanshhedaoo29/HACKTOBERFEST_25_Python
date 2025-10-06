import pytest

@pytest.fixture
def sample_arrays():
    return {
        "basic": [1, 2, 3, 4],
        "mixed": [10, 8, 30, 4, 5],
        "not_found": [10, 8, 30],
        "empty": [],
        "single_match": [1],
        "single_miss": [2],
        "duplicates": [1, 2, 3, 2, 2],
        "first": [5, 6, 7],
        "last": [1, 2, 3, 4],
        "negatives": [-10, -5, 0, 5, 10],
        "strings": ["apple", "banana", "cherry"],
        "mixed_types": [1, "two", 3.0],
    }

@pytest.fixture
def sorted_arrays():
    return {
        "basic": [2, 3, 4, 10, 40],
        "long": [1, 3, 5, 7, 9, 11, 13, 15, 17],
        "single": [5],
        "empty": [],
        "duplicates": [1, 2, 2, 2, 3],
        "negatives": [-10, -5, 0, 5, 10],
        "strings": ["apple", "banana", "cherry", "date"],
    }