#!/usr/bin/python3
""" define a class for rectangle """


class Rectangle:

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for private instance width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """setter for private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter for private instance height"""
        if not isinstance(valur, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
