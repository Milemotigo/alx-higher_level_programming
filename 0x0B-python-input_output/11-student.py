#!/usr/bin/python3
'''Defines a class student'''


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = name
        self.last_name = last
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            Retrieved = {}
            for attr in attrs:
                if hasattr(self, attr):
                    Retrieved[attr] = getattr(self, attr)
            return Retrieved

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
