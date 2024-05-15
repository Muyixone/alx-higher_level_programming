#!/usr/bin/python3

"""A square class that defines a square"""


class Square:
    """A square class that defines a square.

    Args:
        size(int): A private class that computes the area of the square.

   Attributes:
       size(int): A private class that computes the area of the square.

    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
