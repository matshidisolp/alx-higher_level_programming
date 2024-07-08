#!/bin/bash
# sends a JSON POST request to a given URL and display body of the response 
curl -s -X POST -H "Content-Type: application/json" -d @"$FILE" "$URL"
