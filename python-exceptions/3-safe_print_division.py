#!/usr/bin/python3
"""Module that defines a function to safely divide two integers."""


def safe_print_division(a, b):
    """Divide a by b, print the result in finally and return it."""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
