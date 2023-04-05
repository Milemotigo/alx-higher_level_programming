#!/usr/bin/python3

""" define a class for rectangle """


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private instance width"""
        return self.width

    @width.setter
    def width(self, value):
        """setter for private instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            return self._height
        """getter for private instance width"""
        @height.setter
        def height(self, value):
            """setter for private instance width"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
