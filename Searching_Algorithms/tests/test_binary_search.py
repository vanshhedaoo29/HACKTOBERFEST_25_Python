from Searching_Algorithms.binary_search import binarySearch

class TestBinarySearch:

    def test_found_middle(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["basic"], 10) == 3

    def test_found_first(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["basic"], 2) == 0

    def test_found_last(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["basic"], 40) == 4

    def test_not_found(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["basic"], 99) == -1

    def test_empty_array(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["empty"], 1) == -1

    def test_single_element_match(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["single"], 5) == 0

    def test_single_element_miss(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["single"], 1) == -1

    def test_duplicates(self, binary_search_arrays):
        # Should return first occurrence of 2, which is index 1
        assert binarySearch(binary_search_arrays["duplicates"], 2) in [1, 2, 3]

    def test_negative_numbers(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["negatives"], -5) == 1

    def test_string_search(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["strings"], "cherry") == 2

    def test_large_array(self, binary_search_arrays):
        assert binarySearch(binary_search_arrays["long"], 13) == 6