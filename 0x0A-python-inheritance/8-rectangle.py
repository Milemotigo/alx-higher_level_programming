#!/usr/bin/pytyon3
'''Define a class rectangle that inherits from baseGeometry.'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''repesent a rectangle using base geometry.'''
    def __init__(self, width, height):
        '''initializes a new rectangle.
        Args:
            width(int): width of the new rectangle.
            height(int): height pf a new rectangle.
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
