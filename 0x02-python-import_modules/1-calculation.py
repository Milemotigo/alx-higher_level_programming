#!/usr/bin/python3
# 1-calculator.py

if __main__ == "__main__":
    """print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{0} + {1} = {2}".format(a, b, add(a, b)))
    print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    print("{0} / {1} = {2}".format(a, b, div(a, b)))
