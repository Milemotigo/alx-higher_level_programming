#!/usr/bin/python3
'''Json module that write an object to a text file'''
import json


def save_to_json_file(my_obj, filename):
    '''writes an object to a text file
    Arg:
        my_obj: object to write to text file
        filename: name of the object
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
