#!/usr/bin/python3
"""
function to add two integers
"""


def add_integer(a, b=98):
    """
    function takes two integer/floats and returns the sum of the two
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
