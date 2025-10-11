import pytest

# --- LINEAR SEARCH FIXTURE ---
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

# --- BINARY SEARCH FIXTURE ---
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

# --- FIBONACCI SEARCH FIXTURE ---
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

# --- INTERPOLATION SEARCH FIXTURE ---
@pytest.fixture
def interpolation_search_arrays():
    return {
        "basic": [10, 20, 30, 40, 50],
        "small": [5, 10, 15],
        "tiny": [1, 2, 3],
        "all_equal": [7, 7, 7, 7],
        "single": [10],
        "out_of_range": [10, 20, 30],
        "go_left": [10, 11, 12, 12, 12],
    }

# --- JUMP SEARCH FIXTURE ---
@pytest.fixture
def jump_search_arrays():
    return {
        "basic": [1, 2, 3, 4, 5],
        "between_values": [1, 3, 5, 7],
        "beyond_end": [1, 2, 3],
        "empty": [],
        "single_match": [5],
        "single_miss": [5],
        "smaller_than_first": [10, 20, 30],
        "final_return_block": [1, 2, 4, 5],
        "duplicates": [1, 2, 2, 2, 3],
        "block_boundary": [1, 2, 4, 5, 6, 7, 9, 10, 11],
        "various_types_int": [1, 2, 3, 4],
        "various_types_float": [1.0, 2.5, 3.5],
        "various_types_str": ["a", "b", "c"],
    }
