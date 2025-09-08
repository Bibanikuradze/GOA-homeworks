# 3 Create a dictionary with at least five key-value pairs and print all the keys using the keys() method.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer', 'hobbies': 'Reading'}
print("Task 3: Keys in the dictionary:", my_dict.keys())


# 4 Create a dictionary and print all the values using the values() method.
print("\nTask 4: Values in the dictionary:", my_dict.values())


# 5 Create a dictionary and print all key-value pairs using the items() method.
print("\nTask 5: Key-value pairs in the dictionary:", my_dict.items())


# 6 Iterate over a dictionary using the items() method and print each key with its corresponding value.
print("\nTask 6: Iterating over the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")


# 7 Create a dictionary and check if a specific key exists using the in operator.
if 'name' in my_dict:
    print("\nTask 7: Key 'name' exists in the dictionary.")
else:
    print("\nTask 7: Key 'name' does not exist in the dictionary.")


# 8 Retrieve a value from a dictionary using the get() method and handle cases where the key does not exist.
print("\nTask 8: Using get() method:")
print(my_dict.get('country', 'Key not found'))


# 9 Add a new key-value pair to an existing dictionary and print the updated dictionary.
my_dict['country'] = 'USA'
print("\nTask 9: Updated dictionary:", my_dict)


# 10 Remove a key-value pair from a dictionary using the pop() method and print the updated dictionary.
my_dict.pop('hobbies')
print("\nTask 10: Updated dictionary after pop:", my_dict)


# 11 Update an existing dictionary with another dictionary using the update() method.
new_data = {'job': 'Software Engineer', 'location': 'San Francisco'}
my_dict.update(new_data)
print("\nTask 11: Updated dictionary with new data:", my_dict)


# 12 Create a dictionary and print its length using the len() function.
print("\nTask 12: Length of the dictionary:", len(my_dict))


# 13 Write a function that returns the sum of all numeric values in a dictionary.
def sum_numeric_values(d):
    return sum(value for value in d.values() if isinstance(value, (int, float)))

print("\nTask 13: Sum of numeric values in the dictionary:", sum_numeric_values(my_dict))


# 14 Clear all elements from a dictionary using the clear() method and print the result.
my_dict.clear()
print("\nTask 14: Dictionary after clearing:", my_dict)


# 15 Create a dictionary about your information, use at least 10 key-value pairs.
my_info = {
    'name': 'ChatGPT',
    'age': 2,
    'job': 'AI Assistant',
    'language': 'English',
    'location': 'Cloud',
    'hobbies': 'Learning, Assisting, Creating',
    'favorite_food': 'Data',
    'experience': 'Advanced NLP',
    'skills': ['Text Generation', 'Coding', 'Conversational AI'],
    'creator': 'OpenAI'
}

print("\nTask 15: My Information Dictionary:", my_info)