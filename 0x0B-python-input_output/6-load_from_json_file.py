#!/usr/bin/python3
'''Module that creates an object from json'''
import json


def load_from_json_file(filename):
    '''creates object from json
    Arg:
        filename: name of the file
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        json_string = f.read()
        jsonObject = json.loads(json_string)
        return jsonObject
