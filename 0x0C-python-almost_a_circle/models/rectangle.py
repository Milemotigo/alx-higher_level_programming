#!/usr/bin/python3
'''creates a rectangle class'''


from models.base import Base
'''inherit instance from base'''


class Rectangle(Base):
    '''A representation of the rectange of our OOP hierarchy.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Set/get the width of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Set/get the width of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        __self.x = value

    @property
    def y(self):
        """Set/get the width of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
