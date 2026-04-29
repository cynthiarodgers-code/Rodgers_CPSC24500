"""
circle.py - Week 6 

Circle extends Shape. Validate that radius is positive (raise ValueError otherwise).
"""

import math
from shape import Shape


class Circle(Shape):

    def __init__(self, radius):
        # TODO: raise ValueError if radius is not positive
        # TODO: store radius
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        # TODO: return pi * r^2 (use math.pi)
        return math.pi * self.radius ** 2

    def perimeter(self):
        # TODO: return 2 * pi * r
        return 2 * math.pi * self.radius

    def describe(self):
        # TODO: return f"Circle with radius {self._radius}"
        return f"A circle with radius {self.radius}"
