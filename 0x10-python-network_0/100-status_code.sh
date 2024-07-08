#!/bin/bash
# sends a request to given URL and display only the status code of response
curl -so /dev/null -w "%{http_code}" "$1"
