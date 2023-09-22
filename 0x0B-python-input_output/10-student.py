#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    Class defines several public instance attributes i.e
    first name, last name, age of student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize an instance of a class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
