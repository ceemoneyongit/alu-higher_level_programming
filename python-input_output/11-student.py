#!/usr/bin/python3
"""Module that defines a Student class with serialization and reload."""


class Student:
    """A class that defines a student with serialization support."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary of attribute names and values.
        """
        for k, v in json.items():
            setattr(self, k, v)
