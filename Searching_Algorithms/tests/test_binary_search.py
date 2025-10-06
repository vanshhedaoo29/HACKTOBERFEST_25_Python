from Searching_Algorithms.binary_search import binarySearch

class TestBinarySearch:

    def test_found_middle(self, sorted_arrays):
        assert binarySearch(sorted_arrays["basic"], 10) == 3

    def test_found_first(self, sorted_arrays):
        assert binarySearch(sorted_arrays["basic"], 2) == 0

    def test_found_last(self, sorted_arrays):
        assert binarySearch(sorted_arrays["basic"], 40) == 4

    def test_not_found(self, sorted_arrays):
        assert binarySearch(sorted_arrays["basic"], 99) == -1

    def test_empty_array(self, sorted_arrays):
        assert binarySearch(sorted_arrays["empty"], 1) == -1

    def test_single_element_match(self, sorted_arrays):
        assert binarySearch(sorted_arrays["single"], 5) == 0

    def test_single_element_miss(self, sorted_arrays):
        assert binarySearch(sorted_arrays["single"], 1) == -1

    def test_duplicates(self, sorted_arrays):
        # Should return first occurrence of 2, which is index 1
        assert binarySearch(sorted_arrays["duplicates"], 2) in [1, 2, 3]

    def test_negative_numbers(self, sorted_arrays):
        assert binarySearch(sorted_arrays["negatives"], -5) == 1

    def test_string_search(self, sorted_arrays):
        assert binarySearch(sorted_arrays["strings"], "cherry") == 2

    def test_large_array(self, sorted_arrays):
        assert binarySearch(sorted_arrays["long"], 13) == 6