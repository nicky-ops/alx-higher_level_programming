#!/usr/bin/python3
import requests
from sys import argv
"""
this script fetches a URL passed in as an agument using requests package
displays the value of the X-Request-Id variable
"""


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)