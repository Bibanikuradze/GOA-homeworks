# საკლასო დავალება:
# შექმენით dictionary, სადაც იქნება შემდეგი გასაღებები: name, surname, academy, fav-color, city, goa-student, age, fav-programming-lang.
# შემდეგ დაბეჭდეთ ამ dict-ის თითოეული მნიშვნელობა
student_info = {
    'name': 'biba',
    'surname': 'nikuradze',
    'academy': 'goa',
    'fav-color': 'blur',
    'city': 'tbilisi',
    'goa-student': True,
    'age': 15,
    'fav-programming-lang': 'Python , Html'
}

print(student_info)


# Create a Python program that initializes a dictionary with at least five key-value pairs. Perform the following operations:

# Print all the keys in the dictionary using the keys() method.
# Print all the values in the dictionary using the values() method.
# Print all key-value pairs using the items() method.
# Iterate over the dictionary using the items() method and print each key with its corresponding value in a formatted string.
student_info = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'fav_color': 'Blue',
    'is_active': True
}

print("Keys in the dictionary:")
print(student_info.keys())

print("\nValues in the dictionary:")
print(student_info.values())

print("\nKey-Value pairs in the dictionary:")
print(student_info.items())

print("\nFormatted Key-Value pairs:")
for key, value in student_info.items():
    print(f"{key}: {value}")