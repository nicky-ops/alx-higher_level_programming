#!/usr/bin/python3
"""
script takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) <= 1:
        q = ""
    else:
        q = {'q': argv[1]}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=q)
    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
