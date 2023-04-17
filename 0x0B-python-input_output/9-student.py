#!/usr/bin/python3
'''Defines a class of student'''


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        returns a dictionary representation with simple data structure
        '''
        return self.__dict__
