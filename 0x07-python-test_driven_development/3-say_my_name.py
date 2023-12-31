#!/usr/bin/python3
"""
Function to print full names
"""


def say_my_name(first_name, last_name=""):
    """
    takes two arguments first_name an d last_name
    prints first name and last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
