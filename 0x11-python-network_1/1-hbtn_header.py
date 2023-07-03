#!/usr/bin/python3
# Python script that takes in a URL, sends a request tothe url


import urllib.request
import sys


def take_url(url):
    with urllib.request.urlopen(url) as resp:
        headers = resp.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)


url = sys.argv[1]
take_url(url)
