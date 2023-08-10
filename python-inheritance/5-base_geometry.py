#!/usr/bin/python3

"""
5-base_geometry module

This module defines a base class for geometry-related classes. It includes methods for calculating area
and validating integer values.
"""

class BaseGeometry:

    """
    A base class for geometry-related classes.
    """

    def area(self):

         """
        Calculate the area. This method is not implemented and will raise an Exception.

        Raises:
            Exception: Always raises an Exception with the message 'area() is not implemented'.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        Validate an integer value.

        Args:
            name (str): The name associated with the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

