#!/usr/bin/python3
'''Defines a class student'''


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = name
        self.last_name = last
        self.age = age

    def to_json(self, attrs=None):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            Retrieved = {}
            for attr in attrs:
                if hasattr(self, attr):
                    Retrieved[attr] = getattr(self, attr)
            return Retrieved

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
