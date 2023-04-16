#!/usr/bin/python3
'''Defines a text file reading fuction'''


def read_file(filename=""):
    '''opens file in write mode and prints it to the standard output'''

    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()
        print(contents)
