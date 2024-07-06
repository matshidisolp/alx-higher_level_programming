#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest)
of a repository by user.
"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    commits = response.json()

    try:
        for commit in commits[:10]:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    except KeyError:
        print("Error in retrieving data")
