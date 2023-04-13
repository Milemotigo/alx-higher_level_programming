#!/usr/bin/python3
"""define an object lookup function"""



def lookup(obj):
    '''use a list comprhension to get the list'''
    return[attr for attr in dir(obj)]
