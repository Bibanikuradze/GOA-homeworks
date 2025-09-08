# მომხმარებელს შემოატანინეთ 2 რიცხვი და დაბეჭდეთ მათ შორის უდიდესი
num1 = int(input("enter your num: "))
num2 = int(input("enter your num: "))
print(max(num1 , num2))

# Write a program that checks if a given number is even or odd.
number = int(input("enter your num: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Write a program to check if a number is positive or negative.
num1 = float(input("Enter number: "))
if num1 > 0:
    print(num1, "is positive")
else:
    print(num1, "is negative")

# Write a program to check if a number is divisible by 5 - პროგრამა რომელიც ამოწმებს რიცხვი 5-ზე უნაშთოდ იყოფა თუ არა
num2 = float(input("Enter number: "))
if num2 %5 == 0:
    print(num2, "is divisible by five")
else:
    print(num2, "is not divisible by five")

# Ask the user to enter a number multiple times and check if it's even or odd. Stop after 5 numbers.
num3 = int(input("Enter number: "))

if num3 %2 == 0:
    print(num3, "is even")
else:
    print(num3, "is odd")

# Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.
correct_pas = "Goa best"
count = 0
user_password = input("Enter password: ")

while user_password != correct_pas:
    count += 1
    user_password = input("Enter password: ")
print("Correct password!")
print("You needed", count, "tries")

# Write a program that takes two numbers and an operator (+, -, *, /) as input and performs the calculation. Display the result and end the program.

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print("Result:", result)
