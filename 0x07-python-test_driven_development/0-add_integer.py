#!/usr/bin/python3


def add_integer(a, b=98):
    """Adds 2 integers.
    Arguments:
        a: the first int.
        b: second int, default 98.
    Raises:
        TypeError: if a, b are neither int nor float.
    Returns:
        sum of the 2 integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
