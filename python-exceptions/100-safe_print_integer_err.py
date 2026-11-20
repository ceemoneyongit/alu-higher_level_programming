#!/usr/bin/python3
"""Module that defines a function to print an integer with errors."""
import sys


def safe_print_integer_err(value):
    """Print an integer, or print the error in stderr and return False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
