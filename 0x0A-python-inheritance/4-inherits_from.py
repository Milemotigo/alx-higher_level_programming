#!/usr/bin/python3
"""
Module for is_same_class method
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    otherwise returns False.
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
