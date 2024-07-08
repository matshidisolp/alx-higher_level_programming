#!/bin/bash
# sends a request to a request to 0.0.0.0:5000/catch_me that causes
# server to respond with You got me!, in the body of the response
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
