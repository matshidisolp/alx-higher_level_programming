#!/usr/bin/python3
"""Takes a URL, sends a request to the URL,
displays the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the error code.
"""

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
