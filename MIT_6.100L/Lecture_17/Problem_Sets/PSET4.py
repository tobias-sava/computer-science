# 10/04/2025

class Rectangle():
    def __init__(self, width, height):
        """ Initializes self with width and height """
        self.width = width
        self.height = height

    def get_width(self):
        """ Returns the width of self """
        return self.width

    def get_height(self):
        """ Returns the height of self """
        return self.height

    def set_width(self, width):
        """ width is a number
        Changes the width of self to width """
        self.width = width

    def set_height(self, height):
        """ height is a number
        Changes the height of self to height """
        self.height = height

    def get_area(self):
        """ Returns the area of self (width * height) """
        return (self.width * self.height)

    def get_perimeter(self):
        """ Returns the perimeter of self (2 * (width + height)) """
        return (2 * (self.width + self.height))

    def equal(self, r):
        """ r is a Rectangle object
        Returns True if self and r have the same area """
        return self.get_area() == r.get_area()

    def scale(self, factor):
        """ factor is a number
        Scales the width and height of self by the factor """
        self.width = self.width * factor
        self.height = self.height * factor
