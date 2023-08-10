#!/usr/bin/python3
Square = __import__('0-square').Square

"""
This module defines a Square class representing a geometric square.

Classes:
    Square: A class representing a square with a given size.

"""

class Square:
    """
    This class represents a square.
    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes a new Square instance with the     given size.
    """
    
    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """

        self.__size = size


