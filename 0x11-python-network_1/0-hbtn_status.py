#!/usr/bin/python3
"""
this script fetches https://alx-intranet.hbtn.io/status using urllib module
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        body = html.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", body)
