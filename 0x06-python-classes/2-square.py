#!/usr/bin/python3
"""defines class square"""


class Square:
    """empty square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an Integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
