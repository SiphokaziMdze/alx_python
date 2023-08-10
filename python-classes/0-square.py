#!/usr/bin/python3
Square = __import__('0-square').Square

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


