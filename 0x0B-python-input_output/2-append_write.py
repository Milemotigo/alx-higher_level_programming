#!/usr/bin/python3
'''
Defines a module that write into a file
'''


def append_write(filename="", text=""):
    '''write_file write a string to a text file
    Args:
        filename(str): file to write string
        text(str): string to write to file

        Return: number of characters added
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        char_count = file.write(text)
        return char_count
