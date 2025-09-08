# 1: Create a list comprehension that generates a list of numbers from 1 to 10.
numbers_1_to_10 = [x for x in range(1, 11)]
print("Task 1: List of numbers from 1 to 10:", numbers_1_to_10)


# 2: Generate a list of squares of numbers from 1 to 5 using list comprehension.
squares_1_to_5 = [x**2 for x in range(1, 6)]
print("\nTask 2: List of squares from 1 to 5:", squares_1_to_5)


# 3: Create a list of all even numbers between 1 and 20 using list comprehension.
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("\nTask 3: Even numbers between 1 and 20:", even_numbers)


# 4: Generate a list of the first letters of each word in a given list of words using list comprehension.
words = ['apple', 'banana', 'cherry', 'date']
first_letters = [word[0] for word in words]
print("\nTask 4: First letters of each word:", first_letters)


# 5: Create a list comprehension that converts all words in a given list to uppercase.
uppercase_words = [word.upper() for word in words]
print("\nTask 5: Words in uppercase:", uppercase_words)


# 6: Create a list comprehension that generates a list of numbers from 1 to 50 that are divisible by 3.
divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print("\nTask 6: Numbers from 1 to 50 divisible by 3:", divisible_by_3)


# 7: Create a list comprehension that extracts words with more than 4 letters from a given list of words.
long_words = [word for word in words if len(word) > 4]
print("\nTask 7: Words with more than 4 letters:", long_words)


# 8: Create a list comprehension that converts a list of temperature values in Celsius to Fahrenheit.
celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("\nTask 8: Celsius to Fahrenheit:", fahrenheit)


# 9: Create a list comprehension that finds all prime numbers between 1 and 100.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [x for x in range(1, 101) if is_prime(x)]
print("\nTask 9: Prime numbers between 1 and 100:", prime_numbers)


# 10: Create a list comprehension that extracts all words from a given sentence that contain at least one vowel and are longer than 5 characters.
sentence = "Python is a powerful programming language"
words_in_sentence = sentence.split()
words_with_vowel_and_longer_than_5 = [word for word in words_in_sentence if any(vowel in word for vowel in 'aeiou') and len(word) > 5]
print("\nTask 10: Words with at least one vowel and longer than 5 characters:", words_with_vowel_and_longer_than_5)


# 11: Create a list comprehension that generates a sequence of Fibonacci numbers up to the 20th term.
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, 20)]
print("\nTask 11: Fibonacci sequence up to the 20th term:", fibonacci)