#!/usr/bin/python3

"""
4-base_geometry module

This module defines a base class for geometry-related classes and includes an area() method
that raises an Exception when called.
"""

class BaseGeometry:

    """
    An empty base class for geometry-related classes.
    """

    def area(self):

         """
        Calculate the area. This method is not implemented and will raise        an Exception.

        Raises:
            Exception: Always raises an Exception with the message 'area(            ) is not implemented'.
        """

        raise Exception("area() is not implemented")

