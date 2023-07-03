#!/usr/bin/env python3
'''
Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id
'''

import urllib.request
import sys
def take_url(url):
    with urllib.request.urlopen(url) as resp:
        headers = resp.info()
        x_request_id = headers.get("X-Request-Id")
        if x_request_id:
            print(f"X-Request-Id found {x_request_id}")
        else:
            print("X-Request-Id not found")

url = sys.argv[1]
take_url(url)

