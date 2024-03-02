#!/usr/bin/python3
"""
this script takes in a URL argument and an email address
sends a POST request to the passed  URL with the email as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    r = requests.post(url, data=value)
    email = r.text
    print(email)
