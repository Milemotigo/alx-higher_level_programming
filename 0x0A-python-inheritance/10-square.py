#!/usr/bin/python3
'''Define a class square that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defines a new classs named Square'''
    def __init__(self, size):
        '''initializes square attributesi
        Args:
            size(int): size of square
        '''

        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''Define a square attribute for square'''
        return(self.__size * self.__size)
