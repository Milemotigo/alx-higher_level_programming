#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        #attempt to call a function with a given argument
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file = sys.stderr)
        return None
