#!/bin/bash
# sends a request to given URL and cause a specific response
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
