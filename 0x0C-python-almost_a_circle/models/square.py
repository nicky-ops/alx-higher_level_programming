#!/usr/bin/python3
"""
defines a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits attributes from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor - initializes a new square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the class Square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
