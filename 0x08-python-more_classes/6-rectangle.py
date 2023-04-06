#!/usr/bin/python3
"""
defining a rectangle class
"""


class Rectangle:
    """ using the init method for initailizing the object atributes"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """setting the atribute to variable """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2*(self.__width) + 2*(self.__height)

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
            return string

    def __repr__(self):
        return f"Rectangle(self.width, self.height)"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
