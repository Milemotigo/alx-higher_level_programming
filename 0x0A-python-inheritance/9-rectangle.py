#!/usr/bin/python3
'''
Defines a class rectangle that inherits from BaseGeometry.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''define the inherited class'''
    def __init__(self, width, height):
        '''initialize the dimension of Rectangle
        Arg:
            width(int): width of the instance
            height(int): height of the instance
        '''

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        '''
        Return the area of the rectangle
        '''
        area = self.__width * self.__height
        return area

    def __str__(self):
        '''
        Return the string representation of the instance
        '''
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
