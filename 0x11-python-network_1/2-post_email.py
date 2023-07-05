#!/usr/bin/python3
""" 
 This is MODULE:2 - This script takes in a URL + email, sends POST 
 request to the passed URL with the email as a parameter, 
 and displays the body of the response (decoded in utf-8) 
 """
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    def send_email(url, email):
        email_json = {"email": email}
        email_encode = urllib.parse.urlencode(email_json)

        data = email_encode.encode("utf-8")
        seek = urllib.request.Request(url, data, method = 'POST')
        with urllib.request.urlopen(seek) as response:
            display_body = response
            print(display_body.decode("utf-8"))


    url = sys.argv[1]
    email = sys.argv[2]
    send_email(url, email)
