#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL
'''
if __name__ == "__main__":
    import urllib.request
    import sys

    def display_url(url):
        try:
            with urllib.request.urlopen(url) as response:
                result = response.read()
                print(result.decode("utf-8"))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))

    url = sys.argv[1]
    display_url(url)
