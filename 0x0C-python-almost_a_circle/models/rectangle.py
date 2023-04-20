#!/usr/bin/python3
'''inherit from base clase for rectangle'''


from models.base import Base
'''inherit instance from base'''


class Rectangle(Base):
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
    """Set/get the width of the Rectangle."""
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    """Set/get the width of the Rectangle."""
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    """Set/get the width of the Rectangle."""
    def x(self):
        return self.__x

    @x.setter
    """Set/get the width of the Rectangle."""
    def x(self, value):
        __self.x = value

    @property
    """Set/get the width of the Rectangle."""
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
