#!/usr/bin/python3
"""Module that defines a function to execute a function safely."""
import sys


def safe_function(fct, *args):
    """Execute fct with args, return None and print error on failure."""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
