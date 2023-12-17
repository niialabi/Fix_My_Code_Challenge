#!/usr/bin/python3
""" Module containing Square class """


class Square():
    """ square class """

    def __init__(self, *args, **kwargs):
        width = kwargs.get("width", 0)
        height = kwargs.get("height", 0)

        if width != height:
            raise ValueError("Width and height must be equal.")

        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PerimiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimiterOfMySquare())
