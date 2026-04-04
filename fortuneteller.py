print('*-*-*-*-*-*')
print('Welcome to the Fortune Teller!')
print('*-*-*-*-*-*')

name = input("Please enter your full name (first and last name): ")
age = input("Please enter your age (a postive integer): ")

try:
    age = int(age)
    if age <= 0:
        print("Age must be a positive integer.")
except ValueError:
    print("Invalid age input. Please enter an integer.")

color = input("Please enter your favorite color: ")