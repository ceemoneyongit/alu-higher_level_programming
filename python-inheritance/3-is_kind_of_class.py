#!/usr/bin/python3
"""Module that defines a function checking for a class or a subclass."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass."""
    return isinstance(obj, a_class)
