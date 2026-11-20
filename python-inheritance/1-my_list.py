#!/usr/bin/python3
"""Module that defines MyList, a list class that can print itself sorted."""


class MyList(list):
    """A list that inherits from list and adds a sorted print method."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
