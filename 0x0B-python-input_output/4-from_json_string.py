#!/usr/bin/python3
'''Defines a module that convert back string'''
import json


def from_json_string(my_str):
    '''Returns the converted json file
    Arg:
        my_str: json to convert
    '''
    return(json.loads(my_str))
