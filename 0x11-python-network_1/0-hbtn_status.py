#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')

    # Use a with statement to handle the request
    with urlopen(req) as response:
        the_page = response.read()

        # Print the body response details
        print('Body response:')
        print('\t- type:', type(the_page))
        print('\t- content:', the_page)
        print('\t- utf8 content:', the_page.decode('utf-8'))
