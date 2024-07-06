#!/usr/bin/python3
"""Takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    try:
        json_response = response.json()
        print(json_response.get('id'))
    except ValueError:
        print("None")
