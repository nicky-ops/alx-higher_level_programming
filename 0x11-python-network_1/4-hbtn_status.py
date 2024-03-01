#!/usr/bin/python3
"""
this script fetches https://alx-intranet.hbtn.io/status
displays the body of the response
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: ", type(r.text))
    print("\t- content: ", r.text)
