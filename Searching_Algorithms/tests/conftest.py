import pytest

@pytest.fixture
def linear_search_arrays():
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

# Binary Search
@pytest.fixture
def binary_search_arrays():
    return {
        "basic": [2, 3, 4, 10, 40],
        "long": [1, 3, 5, 7, 9, 11, 13, 15, 17],
        "single": [5],
        "empty": [],
        "duplicates": [1, 2, 2, 2, 3],
        "negatives": [-10, -5, 0, 5, 10],
        "strings": ["apple", "banana", "cherry", "date"],
    }

# Fibonacci Search
@pytest.fixture
def fibonacci_search_arrays():
    return {
        "basic": [2, 3, 4, 10, 40],
        "not_found": [2, 3, 4, 10, 40],
        "long": [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100],
        "single_match": [5],
        "single_miss": [7],
        "empty": [],
        "negatives": [-20, -10, -5, 0, 5, 10],
        "strings": ["apple", "banana", "cherry", "date"],
    }

# Jump Search
@pytest.fixture
def jump_search_cases():
    """All jump search test cases in one simple fixture"""
    return [
        # Basic found cases
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        
        # Edge cases
        ([], 1, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([10, 20, 30], 5, -1),
        
        # Not found cases
        ([1, 2, 3], 4, -1),
        ([1, 3, 5, 7], 4, -1),
        ([1, 2, 4, 5], 3, -1),
    ]