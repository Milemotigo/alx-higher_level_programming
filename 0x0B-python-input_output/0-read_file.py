#!/usr/bin/python3
'''Defines a text file reading fuction'''


def read_file(filename=""):

    with open(filename, 'r', encoding='utf-8') as f:
        '''opens file in write mode and prints it to the standard output'''


        contents = f.read()
        print(contents)
