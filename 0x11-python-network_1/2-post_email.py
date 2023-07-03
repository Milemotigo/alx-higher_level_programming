#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    #def send_email(url, email):
    url = sys.argv[1]
    email_json = {"email": sys.argv[2]}
    email_encode = urllib.parse.urlencode(email_json).encode("utf-8")

    data = email_encode

    with urllib.request.urlopen(url, data) as response:
        display_body = response
        print(display_body.decode("utf-8"))

    #url = sys.argv[1]
    #email = sys.argv[2]
    #send_email(url, email)
