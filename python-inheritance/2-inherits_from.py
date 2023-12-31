#!/usr/bin/python3

"""
2-inherits_from module

This module contains a function that checks if an object is an instance of a class that inherited (directly or indirectly)
on a specified class.
"""

def inherits_from(obj, a_class):

    """
    Check if an object is an instance of a class that inherited (directly    or indirectly)
    on the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that is  out of poss        ession of the specified class,
        otherwise False.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class

