#!/usr/bin/python3
'''Defines a string json file converter'''
import json


def to_json_string(my_obj):
    '''Return json representationnof an object
    Arg:
        my_obj: object to convert to json
    '''
    return json.dumps(my_obj)
