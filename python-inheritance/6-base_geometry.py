#!/usr/bin/python3
"""Module that defines a BaseGeometry class with area method."""


class BaseGeometry:
    """A class that defines base geometry with area method."""

    def area(self):
        """Raise an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
