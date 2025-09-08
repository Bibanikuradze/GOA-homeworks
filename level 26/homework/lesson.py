# 2) Sum of Two Numbers: Write a function that takes two numbers as input and returns their sum.
def sum_of_two_numbers(a, b):
    return a + b

result = sum_of_two_numbers(3, 5)
print(result)



# 3) Even or Odd: Create a function that determines whether a given integer is even or odd.
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

result = even_or_odd(7)
print(result)



# 4) Reverse a String: Implement a function that takes a string and returns it reversed.
def reverse_string(s):
    return s[::-1]

result = reverse_string("hello")
print(result)



# 5) Find Maximum: Create a function that takes a list of numbers and returns the maximum value.
def find_maximum(numbers):
    return max(numbers)

numbers = [1, 4, 12, 7, 3]
result = find_maximum(numbers)
print(result)



# 6) Factorial: Implement a function to calculate the factorial of a given number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)
