#!/bin/bash
# send request to URL, display size of response body in bytes
curl -sI "$1" | grep content-length | cut -d ":" -f 2
