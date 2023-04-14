#!/usr/bin/python3
'''
Adds a new attribute to an object if it has a __dict__ attribute
'''


def add_attribute(obj, attrName, attrValue):
    """Method for checking and adding new attribute"""

    if hasattr(obj, '__dict__'):
        obj.__dict__[attrName] = attrValue
    else:
        raise TypeError("can't add new attribute")
