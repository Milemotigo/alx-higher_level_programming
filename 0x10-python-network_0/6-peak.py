#!/usr/bin/python3
"""Defines a peak-finding algorithm"""

def find_peak(list_of_integers):
    if list_of_integers:
        peak = list_of_integers[:-1]
        Max_num = peak[-1]
        return(Max_num)
    else:
        return None