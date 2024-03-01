#!/usr/bin/python3
import urllib.request
from urllib.error import HTTPError
from sys import argv
"""
this script takes a URL argument
displays the body of the response using urllib package
"""


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            body = html.decode('utf-8')
            print(body)
    except HTTPError as err:
        code_err = err.code
        print(f"Error code: {code_err}")
