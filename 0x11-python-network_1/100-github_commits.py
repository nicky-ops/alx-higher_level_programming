#!/usr/bin/python3
"""
script takes GitHub credentials(username and password)
Uses GitHub API to display user's id
"""
import requests
from sys import argv


if __name__ == "__main__":
    repo_name = argv[2]
    owner_name = argv[1]
    url = f"https://api.github.com/repos/{owner_name}/repo_name/commits"
    r = requests.get(url)
    if r.status_code == 200:
        commits = r.json()
        for i in range(10):
            sha = commits[i].get('sha')
            author_name = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
