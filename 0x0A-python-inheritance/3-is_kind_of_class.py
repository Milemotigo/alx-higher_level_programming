#!/usr/bin/python3
'''module for kind of class'''


def is_kind_of_class(obj, a_class):
    '''
    determine if a class has been inherited
    from a parent

    '''
    return isinstance(obj, a_class)
