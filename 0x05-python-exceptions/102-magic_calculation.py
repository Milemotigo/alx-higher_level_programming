#!/usr/bin/python3

import sys
def magic_calculation(a, b):
    #initialize a local variable to zero
    result = 0
    #iterate over the value 1 and 2
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception(Too far)
            #if i<=a
            result = result + a**b / i
        except Exception as e:
            print(e)
            result = a + b
            break
    return result
