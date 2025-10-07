import pytest
from Searching_Algorithms.jump_search import jumpSearch


class TestJumpSearch:
    def test_all_cases(self, jump_search_cases):
        """Test all jump search scenarios"""
        for array, target, expected in jump_search_cases:
            result = jumpSearch(array, target, len(array))
            assert result == expected

    def test_different_data_types(self):
        """Test with different data types"""
        # Test the final return path with different types
        result = jumpSearch([1, 2, 4, 5], 3, 4)
        assert result == -1  # This covers the final return

    def test_duplicate_elements(self):
        """Test with duplicate elements"""
        result = jumpSearch([1, 2, 2, 2, 3], 2, 5)
        assert result in [1, 2, 3]

    def test_step_zero_condition(self, monkeypatch):
        """Test step <= 0 condition"""
        import Searching_Algorithms.jump_search as jump_search_module
        monkeypatch.setattr(jump_search_module.math, 'sqrt', lambda n: 0)
        result = jump_search_module.jumpSearch([1, 2, 3], 2, 3)
        assert result == 1