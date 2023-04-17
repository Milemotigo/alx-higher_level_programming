#!/usr/bin/python3
import json
import sys
from os import path

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == '__main__':
    file_name = 'add_item.json'
    my_list = []
    if path.isfile(file_name):
        my_list = load_from_json_file(file_name)
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, file_name)
