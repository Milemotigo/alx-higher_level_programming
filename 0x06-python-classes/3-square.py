#!/usr/bin/python3
""" defines a square """


class Square:
    """ square with private instance attribute size """
    def __init__(self, size=0):
        """check to make sure that the value is an integer"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        return self.__size ** 2
