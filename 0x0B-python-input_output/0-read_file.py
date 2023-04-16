#!/usr/bin/python3
'''opens the file with (with)'''


def read_file(filename=""):

    with open(filename, 'r', encoding='utf-8') as f:
        '''opens file in write mode encoded'''

        contents = f.read()
        print(contents)
        '''print file in stdout'''
