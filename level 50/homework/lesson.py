# 1) Prompt the user to enter a number. If the input is not a number, display an error message.
try:
    user_input = input("Please enter a number: ")
    number = float(user_input)  # Try converting the input to a number
except ValueError:
    print("Error: That's not a valid number.")

# 2) Create a list and try to access an index that does not exist. Handle IndexError.
my_list = [1, 2, 3]
try:
    print(my_list[5])  # Try accessing an index that doesn't exist
except IndexError:
    print("Error: Index out of range.")

# 3) Try adding an integer to a string and catch the TypeError.
try:
    result = "The number is " + 5  # Attempt to add an integer to a string
except TypeError:
    print("Error: Cannot add an integer to a string.")