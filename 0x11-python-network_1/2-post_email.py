#!/usr/bin/env python3
'''
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response (decoded in utf-8)
'''

if __name__ == '__main__':
    import urllib.parse
    import urllib.request
    import sys


    def send_email(url, email):
        encoded_email = urllib.parse.urlencode({'email': email}).encode('utf-8')
        with urllib.request.urlopen(url, data=encoded_email) as response:
            body = response.read().decode('utf-8')

            print(body)


    url = sys.argv[1]
    email = sys.argv[2]
    send_email(url, email)
