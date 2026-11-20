#!/usr/bin/python3
"""Module that defines a function equivalent to given bytecode."""


def magic_calculation(a, b):
    """Return the result of the calculation described by the bytecode."""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
