#!/usr/bin/python3
#  function that finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    :param list_of_integers: A list of unsorted integers.
    :return: The peak value in the list.
    """
    if list_of_integers:
        peak = list_of_integers[:-1]
        Max_num = peak[-1]
        return(Max_num)
    else:
        return None