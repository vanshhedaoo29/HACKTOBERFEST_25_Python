import pytest

# --- LINEAR SEARCH FIXTURE ---------------------------------------------------
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

# --- BINARY SEARCH FIXTURE ---------------------------------------------------
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

# --- FIBONACCI SEARCH FIXTURE ------------------------------------------------
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

# --- JUMP SEARCH FIXTURE -----------------------------------------------------
@pytest.fixture
def jump_search_basic_cases():
    return [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 3, 5, 7], 4, -1),
        ([1, 2, 3], 4, -1),
        ([], 1, -1),
        ([5], 5, 0),
        ([5], 3, -1),
        ([10, 20, 30], 5, -1),
        ([1, 2, 4, 5], 3, -1),
    ]

@pytest.fixture
def jump_search_duplicates_array():
    return [1, 2, 2, 2, 3]

@pytest.fixture
def jump_search_various_types():
    return [
        ([1, 2, 3, 4], 2, 1),
        ([1.0, 2.5, 3.5], 2.5, 1),
        (["a", "b", "c"], "b", 1),
    ]

@pytest.fixture
def jump_search_block_boundary():
    return [1, 2, 4, 5, 6, 7, 9, 10, 11]

# --- SHARED / GENERIC FIXTURES ----------------------------------------------
@pytest.fixture(scope="session")
def test_metadata():
    """Global configuration for algorithm tests."""
    return {
        "float_tolerance": 1e-9,
        "max_runtime_seconds": 2,
        "categories": ["search", "sort", "graph", "string"],
    }
