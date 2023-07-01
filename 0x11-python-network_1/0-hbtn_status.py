#!/usr/bin/python3
# python script that fetches https://alx-intranet.hbtn.io/status
if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf8')
        print('Body response:')
        print('\t- type:', type(body))
        print('\t- content:', body)
        print('\t- utf8 content:', utf8_content)
