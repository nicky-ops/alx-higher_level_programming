#!/usr/bin/python3
"""
reading a text file
"""


def read_file(filename=""):
    """
    function reads a text file and prints it to stdout
    """

    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
