#!/usr/bin/python3

"""A square class that defines a square"""


class Square:
    """A square class that defines a square.

    Args:
        size(int): A private class that computes the area of the square.

    Attributes:
        size(int): A privat class that computes the area of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """A getter method that returns the square class."""

        return self.__size

    @size.setter
    def size(self, value):
        """A setter method that sets some values to the class.

        Args:
            value(int): Accepts only an integer as parameter.

        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """A getter method that returns the position of the square."""

        return self.__position

    @position.setter
    def position(self, value):
        """A setter method that sets the position of the square.

        Args:
            value(tuple): Accepts on a tuple of two positive integers.

        """

        for item in value:
            if isinstance(item, int) and item >= 0 and item in value[:2]:
                self.__position = value
            else:
                raise TypeError(
                    "position must be a tuple of 2 positive integers"
                )

    def area(self):
        """A method that returns the area of a square."""

        return (self.__size**2)

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()

            for val in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
