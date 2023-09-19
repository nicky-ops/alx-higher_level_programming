#!/usr/bin/python3
"""
Base class for all other classes in the project
"""
import json


class Base:
    """
    Base class contains private class attribute nd_objects.
    Class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return json string representation of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
