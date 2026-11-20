#!/usr/bin/python3
"""Module that defines a function to safely print an integer."""


def safe_print_integer(value):
    """Print value as an integer and return True, otherwise False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
