#!/usr/bin/python3
import urllib.request
from sys import argv
"""
this script fetches a URL passed in as an agument using urllib package
displays the value of the X-Request-Id variable
"""


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
