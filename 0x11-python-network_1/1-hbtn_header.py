#!/usr/bin/python3
""" sends a request to the URL
displays the value of the X-Request-Id
variable found in the header of the response.
"""

import sys
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    with urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-Id')

        print(x_request_id)
