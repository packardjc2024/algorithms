"""
This module uses pytest to test my version of the insertion sort algorithm.
It uses random to create test lists and then demonstrates the different types
of tests that can be run using pytest. It has three different classes to test
cases where the list is empty, the list contains only one element, and the list
contains multiple elements.
"""


import pytest
import random
import configparser
from pathlib import Path

from insertion_sort import insertion_sort
from bubble_sort import bubble_sort


# Create a dictionary of algorithms and their string names
available = {'insertion_sort': insertion_sort,
             'bubble_sort': bubble_sort}


# Get the desired algorithm from the config file
config = configparser.ConfigParser()
config_path = Path.joinpath(Path.cwd(), 'config.ini')
config.read(config_path)
algorithms = []
algorithm = config.get('algorithm', 'current')
algorithms.append(available[algorithm])


# Create a random list and its answer that can be called by the multiple class
# parameterize decorator
random_list = [i for i in range(1, 101)]
random.shuffle(random_list)

multiple_answer = [i for i in range(1, 101)]



@pytest.mark.parametrize('func_name', algorithms)
class TestSortSingle:
    """
    This class tests insertion sort where the list contains only one element.
    """
    answer = [1]
    list_pass = [1]
    list_fail_empty = []
    list_fail_wrong_value = [2]
    list_fail_multiple = [1, 2]

    def test_sort_single_shouldpass(self, func_name):
        """
        The normal usage of the algorithm with one value.
        """
        assert func_name(self.list_pass) == self.answer

    @pytest.mark.xfail
    def test_sort_single_wrong_value_shouldfail(self, func_name):
        """
        Both lists have only one element, however the values are different.
        """
        assert func_name(self.list_fail_wrong_value) == self.answer

    @pytest.mark.xfail
    def test_sort_single_empty_shouldfail(self, func_name):
        """
        Compares the answer list to an empty list.
        """
        assert func_name(self.list_fail_empty) == self.answer

    @pytest.mark.xfail
    def test_sort_single_multiple_shouldfail(self, func_name):
        """
        Compares the answer list to a list with multiple elements.
        """
        assert func_name(self.list_fail_multiple) == self.answer


@pytest.mark.parametrize('func_name', algorithms)
class TestSortEmpty:
    """
    This class tests insertion sort where the list is empty.
    """
    answer = []
    list_pass = []
    list_fail = [1]

    def test_sort_empty_shouldpass(self, func_name):
        """
        Compares the answer to another empty list.
        """
        assert func_name(self.list_pass) == self.answer

    @pytest.mark.xfail
    def test_sort_empty_shouldfail(self, func_name):
        """
        Compares the answer to a list that is not empty.
        """
        assert func_name(self.list_fail) == self.answer


@pytest.mark.parametrize('func_name', algorithms)
class TestSortMultiple:
    """
    This class tests insertion sort where the list contains more than one
    element.
    """
    list_asc = multiple_answer.copy()
    list_desc = sorted(multiple_answer, reverse=True)

    @pytest.mark.parametrize("test_input,expected",
                             [(random.sample(random_list, 100), multiple_answer) for i in range(10)])
    def test_sort_multiple_parametrize(self, func_name, test_input, expected):
        """
        Uses pytest's parametrize to test multiple randomly generated lists at
        once.
        """
        assert func_name(test_input) == expected

    def test_sort_multiple_already_sorted_shouldpass(self, func_name):
        """
        Using the already sorted list, tests the function.
        """
        assert insertion_sort(self.list_asc) == multiple_answer

    @pytest.mark.xfail
    def test_sort_multiple_shouldfail(self, func_name):
        """
        Testing the function by changing the answer to a list out of order in
        order to see if the function fails when it should fail.
        """
        assert func_name(random_list) == self.list_desc
