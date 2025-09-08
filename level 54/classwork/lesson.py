def division_calculator():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        if denominator == 0:
            raise ValueError("Cannot divide by zero!")

        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as e:
        print(f"Error: Invalid input! {e}")

    finally:
        print("Operation complete.")

division_calculator()




def apply_to_list(func, values):
    return [func(value) for value in values]

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_list(square, numbers)

print(squared_numbers)