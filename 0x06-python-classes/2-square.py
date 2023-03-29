#!/usr/bin/python3
"""define a class named Square"""

class Square:
    """define a specail model named init that is called when a new instance of the square is created"""
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
             """create an instance variable named __size and assign it the value size. the self parameter is used to refer to refer to the instance been created"""
        self.__size = size
