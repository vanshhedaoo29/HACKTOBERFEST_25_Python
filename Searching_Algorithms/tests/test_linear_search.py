from Searching_Algorithms.linear_search import search

class TestSearchFunction:

    def test_element_found_middle(self, linear_serach_arrays):
        assert search(linear_serach_arrays["basic"], 3) == 2

    def test_element_found_end(self, linear_serach_arrays):
        assert search(linear_serach_arrays["mixed"], 5) == 4

    def test_element_not_found(self, linear_serach_arrays):
        assert search(linear_serach_arrays["not_found"], 6) == -1

    def test_empty_array(self, linear_serach_arrays):
        assert search(linear_serach_arrays["empty"], 1) == -1

    def test_single_element_match(self, linear_serach_arrays):
        assert search(linear_serach_arrays["single_match"], 1) == 0

    def test_single_element_no_match(self, linear_serach_arrays):
        assert search(linear_serach_arrays["single_miss"], 1) == -1

    def test_multiple_occurrences(self, linear_serach_arrays):
        assert search(linear_serach_arrays["duplicates"], 2) == 1

    def test_first_element(self, linear_serach_arrays):
        assert search(linear_serach_arrays["first"], 5) == 0

    def test_last_element(self, linear_serach_arrays):
        assert search(linear_serach_arrays["last"], 4) == 3

    def test_negative_numbers(self, linear_serach_arrays):
        assert search(linear_serach_arrays["negatives"], -5) == 1

    def test_string_input(self, linear_serach_arrays):
        assert search(linear_serach_arrays["strings"], "banana") == 1

    def test_mixed_types(self, linear_serach_arrays):
        assert search(linear_serach_arrays["mixed_types"], "two") == 1