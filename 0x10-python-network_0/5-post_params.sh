#!/bin/bash
# sends header variables, data to server
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
