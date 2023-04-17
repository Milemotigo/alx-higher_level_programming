#!/usr/bin/python3
'''converts fron object to json'''
import json


def class_to_json(obj):
    '''returns the dictionary description with simple data
    Arg:
        valid: returns a list of valid attributes and method
        value: returns attribute of obj
    '''
    Output = {}
    valid = dir(obj)

    for attr in valid:
        value = getattr(obj, attr)

        if not callable(value) and not attr.startswith('__'):
            Output[attr] = value
    return Output.__dict__
