#!/usr/bin/python3
"""
Contains definition of class MyInt
"""


class MyInt(int):
    '''
    Defines a class that inherit from the int and invert the == and
    != to the default operator
    '''

    def __eq__(self, other):
        '''
        Overide the default operator == and return the default behaviour
        '''
        inverted = super().__ne__(other)
        return inverted

    def __ne__(self, other):
        '''
        Overides the operator == and return the opposite default behaviour
        '''
        inverted = super().__eq__(other)
        return inverted
