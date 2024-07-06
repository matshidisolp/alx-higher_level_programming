#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status
using the requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    response_text = response.text

    print("Body response:")
    print("\t- type:", type(response_text))
    print("\t- content:", response_text)
