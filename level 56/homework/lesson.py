def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None


def expression_matter(a, b, c):
    combs = [
        a+b+c,
        a*b*c,
        (a+b)*c,
        a*(b+c),
        a+(b*c),
        (a*b)+c,
        a*b+c
    ]
    
    return max(combs)


def how_much_i_love_you(nb_petals):
    num=nb_petals % 6
    if num == 0: return "not at all"
    elif num == 1: return "I love you"
    elif num == 2: return "a little"
    elif num == 3: return "a lot"
    elif num == 4: return "passionately"
    elif num == 5: return "madly"


def reverse_list(l):
    return l[::-1]

def reverse_list(l):
    res = []
    for i in range(len(l)-1, -1, -1): res.append(l[i])
    return res

def reverse_list(l):
    return list(reversed(l))

def reverse_list(l):
    l.reverse()
    return l


def odd_count(n):
    return n//2


def find_difference(a, b):
    v_a = a[0] * a[1] * a[2]
    v_b = b[0] * b[1] * b[2]
    
    if v_a > v_b: return v_a - v_b
    return v_b - v_a


def greet(language):
    all_lang = [ 
        ("english", "Welcome")
        , ("czech", "Vitejte")
        , ("danish", "Velkomst")
        , ("dutch", "Welkom")
        , ("estonian", "Tere tulemast")
        , ("finnish", "Tervetuloa")
        , ("flemish", "Welgekomen")
        , ("french", "Bienvenue")
        , ("german", "Willkommen")
        , ("irish", "Failte")
        , ("italian", "Benvenuto")
        , ("latvian", "Gaidits")
        , ("lithuanian", "Laukiamas")
        , ("polish", "Witamy")
        , ("spanish", "Bienvenido")
        , ("swedish", "Valkommen")
        , ("welsh", "Croeso")
    ]
    
    for key in all_lang:
        if key[0] == language: return key[1]
    
    return "Welcome"


def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    

def two_sort(array):
    array.sort()
    
    res = ""
    for i in array[0]:
        res += i+"***"
    
    return res[:-3]


la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


def solution(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a
    

def fix_meerkat(arr):
    return arr[::-1]


def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))


def create_array(n):
    return [i for i in range(1,n+1)]







# 2) Print your name
print("John Doe")

# 3) Print a favorite quote
print('"The only limit to our realization of tomorrow is our doubts of today."')

# 4) Print multiple lines
print("Roses are red")
print("Violets are blue")
print("Coding is fun and so are you!")

# 5) Print a simple math result
print(2 + 3)

# 6) Print a shape with symbols
print("*")
print("**")
print("***")
print("****")

# 7) Convert string to integer
num_str = "42"
num_int = int(num_str)
print(num_int)

# 8) Add two floats
a = 3.5
b = 2.5
print(a + b)

# 9) Concatenate two strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# 10) Print data types
x = 10
y = "Python"
z = 3.14
print(type(x))
print(type(y))
print(type(z))

# 11) User input and type conversion
age = int(input("What is your age? "))
print("Next year you will be", age + 1)

# 12) Ask for your name
name = input("What is your name? ")
print("Hello, " + name + "!")

# 13) Ask for age and calculate next year’s age
age = int(input("How old are you? "))
print("Next year you will be", age + 1)

# 14) Simple calculator: addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is", num1 + num2)

# 15) Favorite color
color = input("What is your favorite color? ")
print("Your favorite color is", color + "!")

# 16) Check if the user is tall enough
height = int(input("Enter your height in cm: "))
if height > 150:
    print("You are tall enough!")
else:
    print("You are not tall enough yet.")

# 17) Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# 18) Print each letter of a string
text = "Python"
for letter in text:
    print(letter)

# 19) Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum is", total)

# 20) Print a multiplication table (1 to 5)
for i in range(1, 6):
    print("2 x", i, "=", 2 * i)

# 21) Print all even numbers between 2 and 20 (inclusive)
for i in range(2, 21, 2):
    print(i)

# 22) Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) Sum of numbers 1 to 5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Sum is", total)

# 24) Count down from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) Print all odd numbers between 1 and 10
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 26) Ask for user input until they enter "exit"
while True:
    user_input = input("Type something (or 'exit' to stop): ")
    if user_input.lower() == "exit":
        break

# 27) Print all elements of a list
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

# 28) Find the length of a list
my_list = [10, 20, 30, 40, 50]
print("Length of the list is", len(my_list))

# 29) Access a specific element from the list
numbers = [10, 20, 30, 40, 50]
print(numbers[1])  # Output: 20

# 30) Add an element to the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# 31) Remove an element from the list
colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)

# 32) Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)

# 33) Create a list of even numbers
even_numbers = [x for x in range(2, 11, 2)]
print(even_numbers)

# 34) Filter odd numbers from a list
nums = [1, 2, 3, 4, 5, 6, 7]
odd_nums = [x for x in nums if x % 2 != 0]
print(odd_nums)

# 35) Convert a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# 36) List of numbers squared if divisible by 2
mixed_nums = [1, 2, 3, 4, 5, 6]
squared_evens = [x**2 for x in mixed_nums if x % 2 == 0]
print(squared_evens)

# 37) Function to greet a user
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")

# 38) Function to add two numbers
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))

# 39) Function to check if a number is even or odd
def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(even_or_odd(7))

# 40) Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 3))

# 41) Function to reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

# 42) Create and print a tuple
my_tuple = (10, "hello", 3.14)
print(my_tuple)

# 43) Access an element in a tuple
t = ("apple", "banana", "cherry", "date")
print(t[1])  # Output: banana

# 44) Find the length of a tuple
print(len(t))

# 45) Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# 46) Check if an item exists in a tuple
items = ("pen", "pencil", "eraser")
if "pencil" in items:
    print("Found")
else:
    print("Not found")

# 47) Create and print a set
my_set = {1, 2, 3}
print(my_set)

# 48) Check if an element is in a set
fruits = {"apple", "banana", "cherry"}
if "banana" in fruits:
    print("Yes")
else:
    print("No")

# 49) Add an element to a set
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)

# 50) Remove an element from a set
nums = {10, 20, 30, 40}
nums.remove(20)
print(nums)

# 51) Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

# 52) Create and print a dictionary
person = {"name": "Alice", "age": 25}
print(person)

# 53) Access a value by key
print(person["name"])  # Output: Alice

# 54) Add a new key-value pair to a dictionary
person["city"] = "New York"
print(person)

# 55) Basic variable assignment
a = "code"  
b = "wa.rs" 
name = a + b  

# 56) get character from ASCII Value
def get_char(c):
    return chr(c)