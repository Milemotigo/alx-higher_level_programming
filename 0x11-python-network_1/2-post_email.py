#!/usr/bin/python3
""" 
 This is MODULE:2 - This script takes in a URL + email, sends POST 
 request to the passed URL with the email as a parameter, 
 and displays the body of the response (decoded in utf-8) 
 """
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    def send_email(url, email):
        email_json = {"email": email}
        email = urllib.parse.urlencode(email_json)

        data = email.encode("utf-8")
        seek = url.request.Request(url, data)
        with urllib.request.urlopen(seek) as response:
            display_body = response
            print(display_body.decode("utf-8"))


    url = sys.argv[1]
    email = sys.argv[2]
    send_email(url, email)
