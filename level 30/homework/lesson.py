# 2) Convert a given sentence to uppercase and print the result.
sentence = input("Enter a sentence: ")
print(sentence.upper())


# 3) Take a user's name input and display it in uppercase letters.
name = input("Enter your name: ")
print(name.upper())


# 4) Create a function that converts a list of lowercase strings to uppercase.
def convert_to_uppercase(strings):
    return [s.upper() for s in strings]
my_list = ['hello', 'world', 'python']
uppercase_list = convert_to_uppercase(my_list)
print(uppercase_list)


# 5) Convert all the characters of a given sentence to lowercase and print it.
sentence = input("Enter a sentence: ")
print(sentence.lower())


# 6) Ask the user for their email address and ensure it is stored in lowercase.
# Ask for user's email address
email = input("Enter your email address: ")
email = email.lower()
print("Your email in lowercase:", email)


# 7) Write a function that takes a mixed-case string and returns it in all lowercase letters.
def to_lowercase(mixed_case_string):
    return mixed_case_string.lower()
result = to_lowercase("PyThOn PrOgRaMmiNg")
print(result)


# 8) Capitalize the first letter of a sentence provided by the user.
sentence = input("Enter a sentence: ")
print(sentence.capitalize())


# 9) Given a list of lowercase strings, capitalize the first letter of each string.
def capitalize_first_letter_of_each_string(strings):
    return [s.capitalize() for s in strings]
my_list = ['hello', 'world', 'python']
capitalized_list = capitalize_first_letter_of_each_string(my_list)
print(capitalized_list)


# 10) Create a function that takes a string and returns it with the first letter capitalized.
def capitalize_first_letter(string):
    return string.capitalize()
result = capitalize_first_letter("hello world")
print(result)


# 11) Find the position of the first occurrence of the word "Python" in a sentence.
sentence = input("Enter a sentence: ")
position = sentence.find("Python")
if position != -1:
    print(f"The word 'Python' first occurs at index {position}.")
else:
    print("The word 'Python' was not found.")


# 12) Search for a user-specified substring in a provided string and print its starting index.
sentence = input("Enter a sentence: ")
substring = input("Enter the substring to search for: ")
position = sentence.find(substring)
if position != -1:
    print(f"The substring '{substring}' first occurs at index {position}.")
else:
    print(f"The substring '{substring}' was not found.")


# 13) Write a function to find and return the index of a specified character in a given string.
def find_char_index(string, char):
    return string.find(char)
result = find_char_index("hello world", "o")
if result != -1:
    print(f"The character 'o' is found at index {result}.")
else:
    print("The character was not found.")


# 14) Find and print the length of a user-provided string.
user_string = input("Enter a string: ")
length = len(user_string)
print(f"The length of the entered string is {length}.")


# 15) Write a function that takes a list of strings and returns their lengths.
def strings_lengths(strings_list):
    return [len(string) for string in strings_list]
my_strings = ['hello', 'world', 'python', 'programming']
lengths = strings_lengths(my_strings)
print(lengths)


# 16) Count the number of times the word "the" appears in a given paragraph.
paragraph = input("Enter a paragraph: ")
word_count = paragraph.lower().split().count("the")
print(f"The word 'the' appears {word_count} times.")


# 17) Ask the user to input a character and count its occurrences in a given string.
string = input("Enter a string: ")
char = input("Enter a character to count its occurrences: ")
char_count = string.count(char)
print(f"The character '{char}' appears {char_count} times in the string.")


# 18) Create a function that counts and returns the occurrences of a specified word in a text.
def count_word_occurrences(text, word):
    return text.lower().split().count(word.lower())
text = "The quick brown fox jumps over the lazy dog. The fox is fast."
word = "the"
word_count = count_word_occurrences(text, word)
print(f"The word '{word}' appears {word_count} times.")


# 19) Find and print the index of the first occurrence of the word "hello" in a given string.
input_string = input("Enter a string: ")
index = input_string.find("hello")
if index != -1:
    print(f"The word 'hello' first appears at index {index}.")
else:
    print("The word 'hello' was not found.")


# 20) Write a function that returns the index of a character provided by the user in a string.
def find_char_index(string, char):
    return string.find(char)
input_string = input("Enter a string: ")
character = input("Enter the character to find its index: ")
index = find_char_index(input_string, character)
if index != -1:
    print(f"The character '{character}' first appears at index {index}.")
else:
    print(f"The character '{character}' was not found.")


# 21) Check if all characters in a given string are lowercase and print the result.
input_string = input("Enter a string: ")
if input_string.islower():
    print("All characters in the string are lowercase.")
else:
    print("Not all characters in the string are lowercase.")


# 22) Create a function that takes a string and returns True if it is completely in lowercase, otherwise False.
def is_lowercase(string):
    return string.islower()
result = is_lowercase("hello world")
print(result)

result2 = is_lowercase("Hello World")
print(result2)


# 23) Prompt the user to input a string and verify if it contains only lowercase letters.
user_string = input("Enter a string: ")
if user_string.islower():
    print("The string contains only lowercase letters.")
else:
    print("The string contains uppercase letters or other characters.")


# 24) Verify if all the characters in a user-provided string are uppercase.
input_string = input("Enter a string: ")
if input_string.isupper():
    print("All characters in the string are uppercase.")
else:
    print("Not all characters in the string are uppercase.")


# 25) Write a function that checks if a string consists entirely of uppercase letters and returns a boolean result.
def is_uppercase(string):
    return string.isupper()

result = is_uppercase("HELLO")
print(result)

result2 = is_uppercase("Hello")
print(result2)


# 26) Check and display whether a string input by the user is in uppercase.
user_string = input("Enter a string: ")
if user_string.isupper():
    print("The string is in uppercase.")
else:
    print("The string is not in uppercase.")


# 27) Replace all occurrences of the word "dog" with "cat" in a given sentence.
sentence = input("Enter a sentence: ")
modified_sentence = sentence.replace("dog", "cat")
print(modified_sentence)


# 28) Write a function that replaces all spaces in a string with underscores.
def replace_spaces_with_underscores(string):
    return string.replace(" ", "_")
input_string = input("Enter a string: ")
result = replace_spaces_with_underscores(input_string)
print(result)


# 29) Convert a string such that uppercase letters become lowercase and vice versa, then print the result.
input_string = input("Enter a string: ")
swapped_string = input_string.swapcase()
print(swapped_string)


# 30) Write a function that takes a sentence and returns it with swapped case for each letter.
def swap_case_in_sentence(sentence):
    return sentence.swapcase()
sentence = input("Enter a sentence: ")
result = swap_case_in_sentence(sentence)
print(result)