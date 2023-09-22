#!/usr/bin/python3
"""
Appending a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    function appends text to filename
    """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
