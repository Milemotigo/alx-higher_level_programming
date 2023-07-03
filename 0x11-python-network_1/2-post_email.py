#!/usr/bin/python3
'''
Python script that takes in a URL and an email, sends a POST requests
'''
if __name__ == "__main__":
    import urllib.request
    import sys

    def take_url_email(url, email):
        data = email.encode('utf-8')  # Encode email as bytes
        req = urllib.request.Request(url, data=data, method='POST')  # Create a POST request
        with urllib.request.urlopen(req) as resp:
            response = resp.read().decode('utf-8')  # Decode the response

        print(response)

    url = sys.argv[1]
    email = sys.argv[2]
    take_url_email(url, email)
