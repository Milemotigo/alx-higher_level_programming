#!/usr/bin/python3
'''
Defines a class that inherit from the int and invert the == and
!= to the default operator
'''


class MyInt(int):
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
