# 1. Creating a variable with an integer value and causing a TypeError with try-except blocks
try:
    num = 10
    result = num + "string"
except TypeError as e:
    print(f"Caught a TypeError: {e}")



# 2. User input with try-except to handle potential errors
try:
    user_input = input("Please enter your name or surname: ")
    age = int(input("Enter your age: "))
    print(f"Your name is {user_input} and you are {age} years old.")
except ValueError as e:
    print(f"Caught a ValueError: {e}")
except Exception as e:
    print(f"Caught an unexpected error: {e}")