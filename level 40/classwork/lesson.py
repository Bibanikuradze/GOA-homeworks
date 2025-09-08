def greet(name):
    return f"Hello, {name} how are you doing today?"

#Function 1 - hello world
def greet():
    return "hello world!"

#Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)

#Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

#You Can't Code Under Pressure #1
def double_integer(i):
    return i*2

#Returning Strings
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

#Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

#Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1+value2
    elif operator == "-":
        return value1-value2
    elif operator == "*":
        return value1*value2
    elif operator == "/":
        return value1/value2

#Keep Hydrated!
def litres(time):
    return time//2

#Century From Year
def century(year):
    return (year + 99) // 100