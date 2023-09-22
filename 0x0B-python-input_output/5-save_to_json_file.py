#!/usr/bin/python3
"""
write an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using JSON representation
    """
    with open(filename, "w", encoding="utf-8") as fl:
        fl.write(json.dumps(my_obj))
