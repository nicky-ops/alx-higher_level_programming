#!/usr/bin/python3
"""defines class square"""


class Square:
    """square class with private instance attribute"""
    def __init__(self, size=0):
        self__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = value
