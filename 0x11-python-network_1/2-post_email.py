#!/usr/bin/env python3

import urllib.parse
import urllib.request
import sys

def send_email(url, email):
    encoded_email = urllib.parse.urlencode({'email': email}).encode('utf-8')  # Encode the email as URL parameters
    with urllib.request.urlopen(url, data=encoded_email) as response:
        body = response.read().decode('utf-8')  # Decode the response body

    print(body)

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_email(url, email)