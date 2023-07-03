#!/usr/bin/python3
'''python script that fetches https://alx-intranet.hbtn.io/status
'''
import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    content = response.json()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
else:
    print("Error:", response.status_code)
