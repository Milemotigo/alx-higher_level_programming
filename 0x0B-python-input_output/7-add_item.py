#!/usr/bin/python3
"""7-add_item.py: Load, add, save"""

import sys
import json
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file ').load_from_json_file


if __name__ == "__main__":

    file_name = add_item.json
    My_list = []

    if path.isfile(file_name):
        my_list = load_from_json_file(sys.argv[1:])

    save_to_json_file(my_list, file_name)
