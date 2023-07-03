#!/usr/bin/python3
'''
python script that takes in a URL, sends a request tothe url
'''
if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        def display_url(url):
            with urllib.request.urlopen(url) as response:
                result = response.read()
                print(result.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:{}".format(e.code))

    url = sys.argv[1]
    display_url(url)
