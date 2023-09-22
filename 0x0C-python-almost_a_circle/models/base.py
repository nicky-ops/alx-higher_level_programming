#!/usr/bin/python3
"""
Base class for all other classes in the project
"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation to a file
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is not None:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
            else:
                jsonfile.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """
        returns the deserialization of a JSON string
        """
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
