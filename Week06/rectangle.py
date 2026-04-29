"""
rectangle.py - Week 6

Rectangle extends Shape. Validate that width and height are both positive.
"""

from shape import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        # TODO: validate both positive (raise ValueError otherwise)
        # TODO: store width and height
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        
        self.width = width
        self.height = height

    def area(self):
        # TODO: width * height
        return self.width * self.height


    def perimeter(self):
        # TODO: 2 * (width + height)
        return 2 * (self.width + self.height)

    def describe(self):
        # TODO: return f"Rectangle {self._width} x {self._height}"
        return f"Rectangle {self.width} x {self.height}"
