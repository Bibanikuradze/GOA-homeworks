# თქვენი სიტყვებით ახსენით რა არის elif და რაში ვიყენებთ მას.
'''else-if ანუ elif-ს ვიყენებთ (if-სა და else-ს შორის)
ანუ თავიდან იწყება if-ით შემდეგ რამდენი elif-იც გვინდა იმდენს გავუწერთ
და ბოლოს თუ საჭირო იქნება დავწერთ else-ს
'''

# Write a program that takes three numbers as input and prints the largest of the three.
num1 = float(input("enter your number: "))
num2 = float(input("enter your number: "))
num3 = float(input("enter your number: "))
largest = max(num1, num2, num3)
print(largest)

# Write a program that takes a score (0-100) as input and outputs the grade based on the following rules:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
score = int(input("enter your number: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = "Invalid score! Please enter a score between 0 and 100."

print("The grade is:", grade)

# Write a program that takes a number as input and prints whether it is positive, negative, or zero.
C = int(input("enter whether o: "))
if C > 0:
    print("positive")
elif C < 0:
    print("negative")
else:
    C == 0
    print("0")

# Use a loop to calculate the sum of numbers between two given integers.
start = int(input("enter num1: "))
end = int(input("enter num2: "))
total_sum = 0
for i in range(start, end + 1):
    total_sum += i
print("The sum of numbers between", start, "and", end, "is:", total_sum)
# Write a program that checks if a single given number is prime number._

# Create a list of five numbers and print the first, third, and last elements using indexing.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First element:", list1[0])
print("Third element:", list1[2])
print("Last element:", list1[-1])
# Create a list of 20 elements (any data type) and print all of the elements - use indexing.
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(len(list2)):
    print(f"Element at index {i}: {list2[i]}")