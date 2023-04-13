#!/usr/bin/python3
'''define the parent class'''


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
