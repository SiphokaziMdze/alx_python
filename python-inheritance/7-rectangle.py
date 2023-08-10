#!/usr/bin/python3

"""
7-rectangle module

This module defines the Rectangle class that inherits from BaseGeometry. It includes methods for calculating
the area of the rectangle and providing a string representation.
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

    def area(self):

        """
        Return a string representation of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):

        """
        Return a string representation of the rectangle.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

