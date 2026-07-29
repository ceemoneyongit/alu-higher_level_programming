#!/usr/bin/python3
"""Module that inserts a line of text to a file after each line
containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string.

    Args:
        filename (str): the name of the file to modify.
        search_string (str): the string to search for in each line.
        new_string (str): the string to insert after each matching line.
    """
    with open(filename) as f:
        lines = f.readlines()
    result = []
    for line in lines:
        result.append(line)
        if search_string in line:
            result.append(new_string)
    with open(filename, "w") as f:
        f.writelines(result)
