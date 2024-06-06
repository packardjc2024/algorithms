"""
My version of the bubble sort algorithm in python. I use a max index  in order
to make the program as efficient as possible sense bubble sort is already not
ideal.
"""


def bubble_sort(numbers_list: list[int]) -> list[int]:
    max_index = len(numbers_list) - 1
    for i in range(max_index):
        index = 0
        while index < max_index:
            if numbers_list[index] > numbers_list[index + 1]:
                numbers_list[index], numbers_list[index + 1] = numbers_list[index + 1], numbers_list[index]
            index += 1
        max_index -= 1

    return numbers_list
