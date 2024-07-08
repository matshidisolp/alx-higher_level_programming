#!/bin/bash
# sends a JSON POST request to a given URL and display body of the response 
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
