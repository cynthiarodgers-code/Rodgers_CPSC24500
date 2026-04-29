"""
main.py - Week 6 

Menu-driven Shape Gallery program.

Menu:
1. Add a circle
2. Add a rectangle
3. Add a triangle
4. Display all shapes
5. Show total area
6. Show largest shape
7. Quit

Wrap input/creation in try/except so the program never crashes on bad input.
"""

from gallery import Gallery
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle


def add_circle(gallery):
    # TODO: prompt for radius, create a Circle, add to gallery
    # Catch ValueError and print a friendly message
    try:
        r = float(input("Enter radius: "))
        gallery.add_shape(Circle(r))
        print("Circle added!")
    except ValueError as e:
        print(f"Error: {e}")


def add_rectangle(gallery):
    # TODO
    try:
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        gallery.add_shape(Rectangle(w, h))
        print("Rectangle added!")
    except ValueError as e:
        print(f"Error: {e}")


def add_triangle(gallery):
    # TODO
    try:
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        c = float(input("Enter side C: "))
        gallery.add_shape(Triangle(a, b, c))
        print("Triangle added!")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    gallery = Gallery("My Shapes")
    # TODO: loop showing the menu and dispatching to the right function
    gallery = Gallery("My Shapes")
    
    while True:
        print("\n--- Shape Gallery Menu ---")
        print("1. Add Circle")
        print("2. Add Rectangle")
        print("3. Add Triangle")
        print("4. Display All Shapes")
        print("5. Show Largest Shape")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            add_circle(gallery)
        elif choice == "2":
            add_rectangle(gallery)
        elif choice == "3":
            add_triangle(gallery)
        elif choice == "4":
            gallery.display_all()
        elif choice == "5":
            largest = gallery.largest_shape()
            if largest:
                print(f"Largest: {largest.describe()} (Area: {largest.area():.2f})")
            else:
                print("Gallery is empty.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
