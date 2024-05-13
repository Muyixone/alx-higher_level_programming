#!/usr/bin/python3

class Square(object):
    """An empty class Square that defines a square.

    Attributes:
        None

    """

    def __getattr__(self, attr):
        """Retrieves the value of the specified attribute.

        Args:
            attr(str): The name of the attribute to retrieve.


        Returns:
            The value of the specified attribute or
            passes if there is an error.

        """
        return None
