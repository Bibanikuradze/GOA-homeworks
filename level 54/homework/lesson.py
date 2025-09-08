def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result of division: {result}")
    except ValueError:
        print("Error: Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")



def access_list_element():
    my_list = ['apple', 'banana', 'cherry']
    try:
        index = int(input(f"Enter an index (0 to {len(my_list)-1}): "))
        print(f"Element at index {index}: {my_list[index]}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer index.")



def access_dict_key():
    my_dict = {'name': 'Alice', 'age': 30}
    key = input("Enter the key to access in the dictionary: ")
    try:
        print(f"Value: {my_dict[key]}")
    except KeyError:
        print("Error: Key does not exist in the dictionary.")



def convert_to_integer():
    user_input = input("Enter a number to convert to integer: ")
    try:
        number = int(user_input)
        print(f"Converted number: {number}")
    except ValueError:
        print("Error: Invalid input, not an integer.")



def greet():
    print("Hello! Have a great day!")



def call_function(func):
    print("Calling the function you passed in...")
    func()



def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier
if __name__ == "__main__":
    divide_numbers()
    access_list_element()
    access_dict_key()
    convert_to_integer()
    call_function(greet)
    times_three = create_multiplier(3)
    print(f"5 multiplied by 3 is: {times_three(5)}")