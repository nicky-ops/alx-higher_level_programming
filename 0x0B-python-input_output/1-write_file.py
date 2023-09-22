#!/usr/bin/python3
"""
Writing a string to a text file
"""


def write_file(filename="", text=""):
    """
    writes a string, text, to a file, filename
    """

    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
