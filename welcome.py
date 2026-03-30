import datetime

user_name = input("Please enter your name: ")

current_year = 2026
pi_approx = 3.14159
is_python_fun = True

now = datetime.datetime.now()

print("*" * 40)
print(f"*** Welcome to my program, {user_name}! ***")
print(f"*** Current Date/Time: {now.strftime('%Y-%m-%d %H:%M:%S')} ***")
print("*" * 40)

print(f"\nDebug Info: Year is {current_year} and Pi is approximately {pi_approx}.")