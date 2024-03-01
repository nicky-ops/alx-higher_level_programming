#!/usr/bin/python3
"""
script takes GitHub credentials(username and password)
Uses GitHub API to display user's id
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    r = requests.get(url, auth=auth)
    if r.status_code == 200:
        data = r.json()
        print(data['id'])
    else:
        print("None")
