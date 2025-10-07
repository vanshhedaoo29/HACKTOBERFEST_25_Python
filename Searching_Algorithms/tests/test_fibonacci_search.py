from Searching_Algorithms.fibonacci_search import fibonacciSearch

class TestFibonacciSearch:

    def test_found_middle(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["basic"], 10) == 3

    def test_found_first(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["basic"], 2) == 0

    def test_found_last(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["basic"], 40) == 4

    def test_not_found(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["not_found"], 11) == -1

    def test_empty_array(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["empty"], 1) == -1

    def test_single_element_match(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["single_match"], 5) == 0

    def test_single_element_miss(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["single_miss"], 5) == -1

    def test_large_array(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["long"], 85) == 8

    def test_negative_numbers(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["negatives"], -10) == 1

    def test_string_search(self, fibonacci_search_arrays):
        assert fibonacciSearch(fibonacci_search_arrays["strings"], "cherry") == 2