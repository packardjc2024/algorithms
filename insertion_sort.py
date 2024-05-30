"""
My version of the insertion sort algorithm in python.
"""


def insertion_sort(nums_list: list[int]) -> list[int]:
    if len(nums_list) <= 1:
        return nums_list
    for i in range(1, len(nums_list)):
        while i > 0:
            if nums_list[i] < nums_list[i - 1]:
                nums_list[i - 1], nums_list[i] = nums_list[i], nums_list[i - 1]
                i -= 1
            else:
                break
    return nums_list


