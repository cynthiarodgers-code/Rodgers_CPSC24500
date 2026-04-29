"""
triangle.py - Week 6 

Triangle extends Shape. Validate:
- All three sides are positive
- Triangle inequality: sum of any two sides must be greater than the third

Use Heron's formula for area:
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
"""

import math
from shape import Shape


class Triangle(Shape):

    def __init__(self, side_a, side_b, side_c):
        # TODO: validate all positive (raise ValueError otherwise)
        # TODO: validate triangle inequality (raise ValueError otherwise)
        # TODO: store the three sides
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides must be positive numbers.")
        
        if not (side_a + side_b > side_c and
                side_a + side_c > side_b and
                side_b + side_c > side_a):
            raise ValueError("The given sides do not form a valid triangle.")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        # TODO: use Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def perimeter(self):
        # TODO: a + b + c
        return self.side_a + self.side_b + self.side_c

    def describe(self):
        # TODO: return f"Triangle with sides {a}, {b}, {c}"
        return f"Triangle with sides {self.side_a}, {self.side_b}, {self.side_c}"
