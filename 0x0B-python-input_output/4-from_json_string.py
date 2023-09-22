#!/usr/bin/python3
"""
return an object from json string
"""
import json


def from_json_string(my_str):
    """
    returns a python object
    """
    return json.loads(my_str)
