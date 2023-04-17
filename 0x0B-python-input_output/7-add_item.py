#!/usr/bin/python3

import sys
import json
from os import path

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    file_name = 'add_item.json'

    if path.isfile(file_name) and path.getsize(file_name) > 0:
        with open(file_name, 'r') as f:
            try:
                my_list = json.load(f)
            except json.JSONDecodeError:
                my_list = []
    else:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, file_name)
