#!/usr/bin/env python3
'''python script that fetches https://alx-intranet.hbtn.io/status
'''
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
