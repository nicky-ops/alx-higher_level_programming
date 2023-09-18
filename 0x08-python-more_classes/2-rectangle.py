#!/usr/bin/python3
"""
Class to define a rectangle
"""


class Rectangle:
    """
    Rectangle class with private instance attributes, height and width
    Getter and setter methods to retrive and set the height and
    width of the rectangle respectively
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.height ==  0 or self.widht == 0:
            return 0
        return (self.height + self.width) * 2
