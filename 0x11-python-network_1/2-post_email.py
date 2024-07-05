#!/usr/bin/python3
"""Takes URL and an email, sends a POST request
to the passed URL with the email as a parameter,
displays the body of the response (decoded in utf-8).
"""

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urlencode({'email': email}).encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
