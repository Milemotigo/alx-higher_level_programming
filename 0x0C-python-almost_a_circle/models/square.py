#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''getters or setters of squaer'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''displays rectangles and args
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3th argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        '''
        arg = args
        if len(arg) >= 1:
            self.id = arg[0]
        if len(arg) >= 2:
            self.size = arg[1]
        if len(arg) >= 3:
            self.x = arg[2]
        if len(arg) >= 4:
            self.y = arg[3]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }
