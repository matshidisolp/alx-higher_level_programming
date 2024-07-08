#!/bin/bash
# sends a JSON POST request to a given URL and display body of the response 
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

URL="$1"
FILE="$2"

curl -s -X POST -H "Content-Type: application/json" -d @"$FILE" "$URL"
