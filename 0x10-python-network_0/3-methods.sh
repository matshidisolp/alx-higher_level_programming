#!/bin/bash
# display all HTTP methods server will accept
curl -IsX OPTIONS "$1" | grep Allow | sed  "s/Allow: //"
