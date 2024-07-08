#!/bin/bash
# sends a request to given URL and display only the status code of response
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"
curl -s -o /dev/null -w "%{http_code}" "$URL"
