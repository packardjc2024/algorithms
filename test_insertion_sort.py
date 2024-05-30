"""
This module uses pytest to test my version of the insertion sort algorithm.
It uses random to create test lists and then demonstrates the different types
of tests that can be run using pytest. It has three different classes to test
cases where the list is empty, the list contains only one element, and the list
contains multiple elements.
"""


import pytest
from insertion_sort import insertion_sort
import random


class TestInsertionSortSingle:
    """
    This class tests insertion sort where the list contains only one element.
    """
    answer = [1]
    list_pass = [1]
    list_fail_empty = []
    list_fail_multiple = [1, 2]

    def test_insertion_sort_single_shouldpass(self):
        assert insertion_sort(self.list_pass) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_single_empty_shouldfail(self):
        assert insertion_sort(self.list_fail_empty) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_single_multiple_shouldfail(self):
        assert insertion_sort(self.list_fail_multiple) == self.answer


class TestInsertionSortEmpty:
    """
    This class tests insertion sort where the list is empty
    """
    answer = []
    list_pass = []
    list_fail = [1]

    def test_insertion_sort_empty_shouldpass(self):
        assert insertion_sort(self.list_pass) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_empty_shouldfail(self):
        assert insertion_sort(self.list_fail) == self.answer


class TestInsertionSortMultiple:
    """
    This class tests insertion sort where the list contains more than one
    element.
    """
    answer = [i for i in range(1, 101)]
    list_asc = answer.copy()
    list_desc = sorted(answer, reverse=True)
    random_list = random.sample(answer, len(answer))

    def test_insertion_sort_shouldpass(self):
        """
        Using a randomly generated list, compares the function's results to
        the answer list.
        """
        assert insertion_sort(self.random_list) == self.answer

    def test_insertion_sort_already_sorted_shouldpass(self):
        """
        Using the already sorted list, tests the function.
        """
        assert insertion_sort(self.list_asc) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_shouldfail(self):
        """
        Testing the function by changing the answer to a list out of order in
        order to see if the function fails when it should fail.
        """
        assert insertion_sort(self.random_list) == self.list_desc

    @pytest.mark.parametrize("input,expected",
                             [(random.sample([i for i in range(1, 101)], 100), [i for i in range(1, 101)]) for i in range(10)])
    def test_insertion_sort_parametrize(self, input, expected):
        """
        Uses pytest's parametrize to test multiple randomly generated lists at
        once.
        """
        assert insertion_sort(input) == expected



