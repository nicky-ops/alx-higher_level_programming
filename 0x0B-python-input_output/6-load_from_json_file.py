#!/usr/bin/python3
"""
creating an object from a JSON file'
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    """

    with open(filename, encoding="utf-8") as fl:
        return json.load(fl)
