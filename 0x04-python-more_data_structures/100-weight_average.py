#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    top_value = 0
    bottom_value = 0
    for tup in my_list:
        top_value += tup[0] * tup[1]
        bottom_value += tup[0]
        return top_value/bottom_value
