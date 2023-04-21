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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Set/get the width of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Set/get the width of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Set/get the width of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        '''return the area of a rectangle'''
        ar = (self.__height * self.__width)
        return(ar)

    def display(self):
        '''display a rectangle'''
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        '''Returns a string representation of a rectangle'''
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x,  self.__y, self.__width, self.__height))

    def display(self):
        '''displays a rectangle and coordinates'''
        for i in range(self.__y):
            print('')
        for i in range(self.__height):
            for i in range(self.__x):
                print(' ', end='')
            for i in range(self.__width):
                print('#', end='')
            print('')

    def update(self, *args):
        '''displays rectangles and args
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        '''
        arg = args
        if len(arg) >= 1:
            self.__id = arg[0]
        if len(arg) >= 2:
            self.__width = arg[1]
        if len(arg) >= 3:
            self.__height = arg[2]
        if len(arg) >= 4:
            self.__x = arg[3]
        if len(arg) >= 5:
            self.__y = arg[4]
