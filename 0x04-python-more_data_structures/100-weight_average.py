#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    top_value = 0
    bottom_value = 0
    for score, weight in my_list:
        top_value += weight * score
        bottom_value += score
        return top_value/bottom_value
