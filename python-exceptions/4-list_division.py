#!/usr/bin/python3
"""Module that defines a function to divide two lists."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide two lists element by element and return a new list."""
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
