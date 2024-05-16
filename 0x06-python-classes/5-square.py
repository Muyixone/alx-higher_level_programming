#!/usr/bin/python3

"""A square class that defines a square"""


class Square:
    """A square class that defins a square.

    Args:
        size(int): A private class that computes the area of the square.

    Attributes:
        size(int): A private class that computes the area of the square.

    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """A getter method that returns the square class."""

        return self.__size

    @size.setter
    def size(self, value):
        """A setter method that sets some values to the class.

        Args:
            value(int): Accepts only an integer as paramer.

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """A method that returns the area of a square.

        Returns:
            The area of the square.

        """

        return (self.__size**2)

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self.size > 0:
            for val in range(self.size):
                for v in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
