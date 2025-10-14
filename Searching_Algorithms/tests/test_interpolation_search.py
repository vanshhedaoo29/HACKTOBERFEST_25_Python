from Searching_Algorithms.interpolation_search import interpolationSearch


def test_found_middle(interpolation_search_arrays):
    arr = interpolation_search_arrays["basic"]
    assert interpolationSearch(arr, 0, len(arr) - 1, 30) == 2


def test_found_first(interpolation_search_arrays):
    arr = interpolation_search_arrays["small"]
    assert interpolationSearch(arr, 0, len(arr) - 1, 5) == 0


def test_found_last(interpolation_search_arrays):
    arr = interpolation_search_arrays["tiny"]
    assert interpolationSearch(arr, 0, len(arr) - 1, 3) == 2


def test_all_equal_found_and_not_found(interpolation_search_arrays):
    arr = interpolation_search_arrays["all_equal"]
    assert interpolationSearch(arr, 0, len(arr) - 1, 7) == 0
    assert interpolationSearch(arr, 0, len(arr) - 1, 5) == -1


def test_single_element_found_and_not_found(interpolation_search_arrays):
    arr = interpolation_search_arrays["single"]
    assert interpolationSearch(arr, 0, 0, 10) == 0
    assert interpolationSearch(arr, 0, 0, 5) == -1


def test_not_found_within_range_triggers_recursion_and_final_minus_one(interpolation_search_arrays):
    arr = interpolation_search_arrays["basic"]
    assert interpolationSearch(arr, 0, len(arr) - 1, 35) == -1


def test_not_found_out_of_range_low_and_high(interpolation_search_arrays):
    arr = interpolation_search_arrays["out_of_range"]
    assert interpolationSearch(arr, 0, len(arr) - 1, 5) == -1
    assert interpolationSearch(arr, 0, len(arr) - 1, 100) == -1


def test_low_greater_than_high_returns_minus_one(interpolation_search_arrays):
    arr = interpolation_search_arrays["out_of_range"]
    assert interpolationSearch(arr, 2, 1, 20) == -1


def test_go_left_branch_recursion(interpolation_search_arrays):
    arr = interpolation_search_arrays["go_left"]
    result = interpolationSearch(arr, 0, len(arr) - 1, 11)
    assert result == 1
