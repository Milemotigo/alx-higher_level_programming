#!/usr/bin/python3
"""Defines a peak-finding algorithm"""


def find_peak(list_of_integers):
   if list_of_integers:
       peak = list_of_integers[:-1]
       Max_num = peak[-1]
       return(Max_num)
   else:
      return None

def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    :param list_of_integers: A list of unsorted integers.
    :return: The peak value in the list.
    """
    if len(list_of_integers) >= 2:
        return list_of_integers[-2]
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        return None   
