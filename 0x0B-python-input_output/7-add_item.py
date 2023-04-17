#!/usr/bin/python3
"""
    Python script that adds all args to a Python List.
    List is then saved to a file.
"""


import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    file_name = "add_item.json"
    json_list = []

    if os.path.exists(file_name):
        json_list = load_from_json_file(file_name)

        json_list.extend(sys.argv[1:])
        save_to_json_file(json_list, file_name)
