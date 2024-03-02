#!/usr/bin/python3
"""
this script fetches https://alx-intranet.hbtn.io/status using urllib module
"""
import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    params = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, params)
    with urllib.request.urlopen(req) as response:
        email = response.read().decode('utf-8')
        print(email)
