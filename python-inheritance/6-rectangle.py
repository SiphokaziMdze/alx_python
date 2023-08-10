#!/usr/bin/python3

"""
6-rectangle module

This module defines the Rectangle class that inherits from BaseGeometry. It includes methods for calculating
area and validating integer values for width and height.
"""

class BaseGeometry:

    """
    A base class for geometry-related classes.
    """

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):

        """
        Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

