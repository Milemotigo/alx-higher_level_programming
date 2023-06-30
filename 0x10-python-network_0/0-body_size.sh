#!/bin/bash
# Send request to URL, display size of response body in bytes
curl -sI "$1" | awk '/content-length/ {print $2}'
