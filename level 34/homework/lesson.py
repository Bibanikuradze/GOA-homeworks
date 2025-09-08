# 2) Function Basics: Write a function that takes no arguments and simply prints "Hello, World!"
def hello_world():
    print("Hello, World!")


# 3) Arguments and Parameters: Write a function that takes two numbers as arguments and prints their sum.
def add_numbers(num1, num2):
    print(num1 + num2)


# 4) Return Statement: Create a function that takes a number as input, multiplies it by 10, and returns the result.
def multiply_by_10(number):
    return number * 10


# 5) Default Arguments: Define a function that takes a name as input and prints a greeting. If no name is provided, it should use "Guest" as the default.
def greet(name="Guest"):
    print(f"Hello, {name}!")


# 6) Boss Level: Nested Functions: Define a function that contains another function inside it and calls the inner function.
def outer_function():
    def inner_function():
        print("This is the inner function!")
    print("This is the outer function!")
    inner_function()


# 7) Write a function that takes a list of numbers and checks whether each number is even or odd using a loop and conditional statements. Print "Even" for even numbers and "Odd" for odd numbers.
def check_even_odd(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")


# 8) Find the Maximum: Create a function that takes a list of numbers and uses a loop to find and return the maximum number.
def find_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num


# 9) Define a function that takes a list of integers and returns a new list containing only the positive numbers. Use a loop and a conditional statement.
def filter_positive_numbers(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers


# 10) Write a function that iterates through a range of numbers (e.g., 1 to 100) and sums up all the numbers divisible by 3. Return the total sum.
def sum_divisible_by_3(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            total += num
    return total


# Example function calls to demonstrate all the functionality

# Function Basics
hello_world()

# Arguments and Parameters
add_numbers(5, 7)

# Return Statement
result = multiply_by_10(5)
print(f"Result of multiplication: {result}")

# Default Arguments
greet("Alice")
greet()

# Boss Level: Nested Functions
outer_function()

# Check Even or Odd
check_even_odd([1, 2, 3, 4, 5, 6])

# Find the Maximum
max_number = find_max([10, 3, 7, 25, 12])
print(f"The maximum number is {max_number}")

# Filter Positive Numbers
positive_nums = filter_positive_numbers([-1, 3, -4, 5, 0, -2, 8])
print(f"Positive numbers: {positive_nums}")

# Sum Numbers Divisible by 3
result = sum_divisible_by_3(1, 100)
print(f"The sum of numbers divisible by 3 from 1 to 100 is {result}")