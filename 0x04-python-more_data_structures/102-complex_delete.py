#!/usr/bin/python3
def complex_delete(a_dict, value):
    key_to_delete = []
    for key in a_dict:
        if a_dict[key] == value:
            key_to_delete.append(key)
        for key in key_to_delete:
            del a_dict[key]
        return a_dict
