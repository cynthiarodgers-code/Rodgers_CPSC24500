"""
gallery.py - Week 6 

The Gallery class uses COMPOSITION. It HAS shapes -- it does NOT inherit from Shape.
Internally it stores a list of Shape objects.
"""


class Gallery:

    def __init__(self, name):
        # TODO: store the name
        # TODO: create an empty list for shapes
        self.name = name
        self.shapes = []

    def add_shape(self, shape):
        # TODO: append the shape to the internal list
        self.shapes.append(shape)

    def total_area(self):
        # TODO: return the sum of all shape areas (0.0 if empty)
        return sum(shape.area() for shape in self.shapes)

    def largest_shape(self):
        # TODO: return the shape with the biggest area (None if empty)
        if not self.shapes:
            return None
        return max(self.shapes, key=lambda s: s.area())

    def display_all(self):
        # TODO: print the gallery name, the count, and each shape's
        #       description, area, and perimeter
        print(f"Gallery: {self.name}")
        print(f"Total Shapes: {len(self.shapes)}")
        print("-" * 20)
        
        for shape in self.shapes:
            print(f"{shape.describe()}")
            print(f"  Area: {shape.area():.2f}")
            print(f"  Perimeter: {shape.perimeter():.2f}")
            print("-" * 10)
