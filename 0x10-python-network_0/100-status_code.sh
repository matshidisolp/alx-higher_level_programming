#!/bin/bash
# sends a request to given URL and display only the status code of response
URL="$1"
curl -s -o /dev/null -w "%{http_code}" "$URL"
