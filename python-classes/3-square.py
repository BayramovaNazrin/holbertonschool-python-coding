#!/usr/bin/python3
"""
Defines a class Square with size property, validation, and area method.
"""


class Square:
    """Represents a square with size validation through getter and setter."""

    def __init__(self, size=0):
        self.size = size  # use the setter for validation

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size
