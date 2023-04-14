#!/usr/bin/python3
'''Defines a class square that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defines a new class Square'''
    def __init__(self, size):
        '''Initializes a square attribute
        Arg:
            size(): size of the square
        '''
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''
        Returns  area of the square
        '''
        return(self.__size * self.__size)

    def __str__(self):
        '''
        Returns printed string of the square
        '''
        return'[{}] {}/{}'.format(
                type(self).__name__,
                self.__size,
                self.__size
                )
