# 2) Add 5 to a given number
add_five = lambda x: x + 5

# 3) Multiply two numbers
multiply = lambda x, y: x * y

# 4) Check if a number is even
is_even = lambda x: x % 2 == 0

# 5) Convert Celsius to Fahrenheit
c_to_f = lambda c: (c * 9/5) + 32

# 6) Check if a string starts with 'A'
starts_with_A = lambda s: s.startswith('A')

# Sample lists
nums = [1, 2, 3, 4, 5]
names = ["alice", "bob", "anna", "mike"]
temps_celsius = [0, 20, 30, 100]
words = ["hello", "world", "python"]
mixed_numbers = [45, 60, 25, 10]

# 7) Add 10 to every number
add_10 = list(map(lambda x: x + 10, nums))

# 8) Convert strings to uppercase
upper_names = list(map(lambda s: s.upper(), names))

# 9) Find length of each word
word_lengths = list(map(lambda w: len(w), words))

# 10) Square each number
squares = list(map(lambda x: x**2, nums))

# 11) Convert integers to strings
str_nums = list(map(lambda x: str(x), nums))

# 12) Concatenate "Hello " to each name
greetings = list(map(lambda name: "Hello " + name, names))

# 13) Subtract 5 from each element
subtract_5 = list(map(lambda x: x - 5, nums))

# 14) Multiply each number by 3
times_3 = list(map(lambda x: x * 3, nums))

# 15) Convert Celsius to Fahrenheit
fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps_celsius))

# 16) Check if numbers are greater than 50
greater_than_50 = list(map(lambda x: x > 50, mixed_numbers))

# Sample lists
nums2 = [5, 8, 12, 15, 22, 30]
strings = ["apple", "", "banana", "kiwi", "", "orange"]
more_nums = [-3, 0, 7, 14, -9, 18]
names2 = ["Alice", "Bob", "Andrew", "Steve"]
words2 = ["pen", "cup", "notebook", "eraser"]
nullable = [None, "a", "", None, "hello", 0]
mixed = [20, 40, 55, 75, 30]

# 17) Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, nums2))

# 18) Numbers greater than 10
greater_than_10 = list(filter(lambda x: x > 10, nums2))

# 19) Strings longer than 5 characters
long_strings = list(filter(lambda s: len(s) > 5, strings))

# 20) Remove empty strings
non_empty = list(filter(lambda s: s != "", strings))

# 21) Positive numbers only
positive_nums = list(filter(lambda x: x > 0, more_nums))

# 22) Names that start with 'A'
a_names = list(filter(lambda name: name.startswith('A'), names2))

# 23) Numbers divisible by 3
div_by_3 = list(filter(lambda x: x % 3 == 0, nums2))

# 24) Words that contain the letter 'e'
words_with_e = list(filter(lambda w: 'e' in w, words2))

# 25) Remove None values
non_none = list(filter(lambda x: x is not None, nullable))

# 26) Numbers less than or equal to 50
less_equal_50 = list(filter(lambda x: x <= 50, mixed))