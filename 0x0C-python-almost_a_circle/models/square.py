#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class"""

        # Call the constructor of the Rectangle class using super()
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""

        # Validation of value same as for width in Rectangle
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return dictionary representation of Square"""

        # Create and return a dictionary with required attributes
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """String representation of Square"""

        return "[Square] ({}) {}/{} - {}".format(
                 self.id, self.x, self.y, self.width
                 )


if __name__ == "__main__":
    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
