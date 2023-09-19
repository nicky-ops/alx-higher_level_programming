#!/usr/bin/python3
"""
Base class for all other classes in the project
"""


class Base:
    """
    Base class contains private class attribute nd_objects.
    Class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
