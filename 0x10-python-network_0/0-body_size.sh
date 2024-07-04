#!/bin/bash
# get the response content length
curl -Is "$1" | grep Content-Length | cut -f 2 -d ':'
