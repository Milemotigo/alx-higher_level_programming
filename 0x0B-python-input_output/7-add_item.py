#!/usr/bin/python3
'''
python script the adds all argument to a python list
'''


import sys
from os import path
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    file_name = add_item.json
    j_List = []

    if path.isfile(file_name):
        j_List = load_from_json_file(file_name)
        for i in range(1, len(sys.argv)):
            json_list.append(sys.argv[i])
        save_to_json_file(j_List, file_name)
