#!/bin/bash
# Display the body of a 200 status code response

#curl -sI "$1" | grep -d 200 && curl -s "$1"
curl -sL "$1"
