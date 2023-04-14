#!/usr/bin/python3
'''module for basegeometry class'''


class BaseGeometry():
    '''
    method for area of class
    '''
    def area(self):
        '''
        raises an Exception with the message area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value < 0:
            raise ValueError("<name> must be greater than 0")
