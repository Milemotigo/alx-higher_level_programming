#!/usr/bin/python3
'''returns the dictionary description with simple data'''
import json


def class_to_json(obj):
    Output = {}

    valid = dir(obj)
    for attr in valid:
        value = getattr(obj, attr)

        if not callable(value) and not attr.startswith('__'):
            Output[attr] = value
    return Output
