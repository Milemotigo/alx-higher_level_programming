#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    utf8_content = body.decode('utf8')
    print('Body response:')
    print('\t - type:', type(body))
    print('\t - content:', body)
    print('\t - utf8 content:', utf8_content)

