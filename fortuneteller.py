import random

print('*-*-*-*-*-*')
print('Welcome to the Fortune Teller!')
print('*-*-*-*-*-*')


name = input("Please enter your full name (first and last name): ")
age = float(input("Please enter your age (a postive integer): "))
color = input("Please enter your favorite color: ")

lucky_number = float(random.randint(1,10))

lucky_percent = (lucky_number / age)

fortunes = [
    "You will find a gem today. ",
    "Success is coming your way. ",
    "Believe in yourself and you can do anything. ",
    "Expect a surprise visit from an old friend. ",
    "Always remember that you are loved. ",
    "Your hard work will pay off soon. ",
    "Enjoy this day like it's your last. ",
    "Call someone and tell them you love them. "
]
selected_fortune = random.choice(fortunes)

try:
    age = int(age)
    if age > 0:
        print("Your age was recorded.")
    else:
        print("Error: Age must be a positive number.")
        
except ValueError:
    print("Invalid age input. Please enter an integer.")



if 1 <= lucky_number <= 3:
    category = "Patience"
elif 4 <= lucky_number <= 6:
    category = "Adventure"
elif 7 <= lucky_number <= 10:
    category = "Prosperity"
else:
    category = "Mystery"
    

name_trimmed = name.strip()
print("\n--- Your Fortune Summary ---")
print(f"Name: {name_trimmed.upper()}")
print(f"Name length: {len(name_trimmed)} characters")
print(f"Age: {age}")
print(f"Favorite Color: {color.lower()}")
print(f"Lucky Number: {lucky_number}")
print(f"Category: {category}")
print(f"Lucky Percentage: {round(lucky_percent * 100)}")
print(f"Fortune: {selected_fortune}")
print("")
with open("fortune_output.txt", "w") as f:
    print("Fortune saved to fortune_output.txt.")
print("")
print("************************************")
print("Goodbye Cynthia! Fortune awaits you!")
print("************************************")


