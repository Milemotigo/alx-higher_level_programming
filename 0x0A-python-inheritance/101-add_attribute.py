#!/usr/bin/python3
'''
Adds a new attribute to an object if it has a __dict__ attribute
:obj: object to add an attribute
:attrName: name of the new attribute
:attrValue: value of the new attribute
'''


def add_attribute(obj, attrName, attrValue):
    if hasattr(obj, '__dict__'):
        obj.__dict__[attrName] = attrValue
    else:
        raise TypeError("can't add new attribute")
