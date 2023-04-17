#!/usr/bin/python3
'''Defines a student class'''


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            Retrieved_attr = {}
            for attr in attrs:
                if hasattr(self, attr):
                    Retrieved_attr[attr] = getattr(self, attr)
            return Retrieved_attr
