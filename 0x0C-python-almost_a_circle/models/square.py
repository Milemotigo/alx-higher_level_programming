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
