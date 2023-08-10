#!/usr/bin/python3

"""
8-square module

This module defines the Square class that inherits from Rectangle. It includes methods for calculating
the area of the square and providing a string representation.
"""

class BaseGeometry:
    """
    A base class for geometry-related classes.
    """

class Square(Rectangle):

    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):

        """
        Initialize a Square instance with size.

        Args:
            size (int): The size of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):

        """
        Return a string representation of the rectangle.
        """

        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

