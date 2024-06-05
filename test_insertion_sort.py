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
    list_fail_wrong_value = [2]
    list_fail_multiple = [1, 2]

    def test_insertion_sort_single_shouldpass(self):
        """
        The normal usage of the algorithm with one value.
        """
        assert insertion_sort(self.list_pass) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_single_wrong_value_shouldfail(self):
        """
        Both lists have only one element, however the values are different.
        """
        assert insertion_sort(self.list_fail_wrong_value) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_single_empty_shouldfail(self):
        """
        Compares the answer list to an empty list.
        """
        assert insertion_sort(self.list_fail_empty) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_single_multiple_shouldfail(self):
        """
        Compares the answer list to a list with multiple elements.
        """
        assert insertion_sort(self.list_fail_multiple) == self.answer


class TestInsertionSortEmpty:
    """
    This class tests insertion sort where the list is empty.
    """
    answer = []
    list_pass = []
    list_fail = [1]

    def test_insertion_sort_empty_shouldpass(self):
        """
        Compares the answer to another empty list.
        """
        assert insertion_sort(self.list_pass) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_empty_shouldfail(self):
        """
        Compares the answer to a list that is not empty.
        """
        assert insertion_sort(self.list_fail) == self.answer


class TestInsertionSortMultiple:
    """
    This class tests insertion sort where the list contains more than one
    element.
    """
    answer = [i for i in range(1, 101)]
    list_asc = answer.copy()
    list_desc = sorted(answer, reverse=True)
    random_list = answer.copy()
    random.shuffle(random_list)

    @pytest.mark.parametrize("test_input,expected",
                             [(random.sample([i for i in range(1, 101)], 100),
                               [i for i in range(1, 101)]) for i in range(10)])
    def test_insertion_sort_multiple_parametrize(self, test_input, expected):
        """
        Uses pytest's parametrize to test multiple randomly generated lists at
        once.
        """
        assert insertion_sort(test_input) == expected

    def test_insertion_sort_multiple_already_sorted_shouldpass(self):
        """
        Using the already sorted list, tests the function.
        """
        assert insertion_sort(self.list_asc) == self.answer

    @pytest.mark.xfail
    def test_insertion_sort_multiple_shouldfail(self):
        """
        Testing the function by changing the answer to a list out of order in
        order to see if the function fails when it should fail.
        """
        assert insertion_sort(self.random_list) == self.list_desc
