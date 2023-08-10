#!/usr/bin/python3

"""
0-is_same_class module

This module contains a function that checks whether an object is an instance of a specified class.

"""

def is_same_class(obj, a_class):

    """
    Check if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class, otherwi        se False.
    """

    return type(obj) is a_class

