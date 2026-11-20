#!/usr/bin/python3
"""Module that defines a function to safely print list integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers of a list and return how many."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
