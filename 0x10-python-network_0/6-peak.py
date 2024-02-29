#!/usr/bin/python3
"""
function find_peak finds a peak in a list of unsorted integers

arguments:
    list_of_integers - an unsorted list of integers
"""
def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    # Binary search approach
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # Move right if mid is less than its right neighbor
            left = mid + 1
        else:
            # Move left if mid is greater than or equal to its right neighbor
            right = mid

    return list_of_integers[left]
