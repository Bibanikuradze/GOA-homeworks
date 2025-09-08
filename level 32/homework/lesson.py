# 2) თქვენი სიტყვებით ახსენით რა განსხვავებაა format ფუნქციასა და f სთრინგს შორის, ასევე რა განსხვავებაა append-სა და insert-ს შორის
'''
format ფუნქცია გამოიყენება როდესაც გვაქვს გარკვეული რაოდენოდის ცვლადე შექმნილი თავისი ინფორმაციით,
ეს ცვლადები უნდა გადავანაწილით იმ წინადადებაში რომელსაც ვბეჭდავთ. წინადადებაში რასაც ვბეჭდავთ სადაც გვინდა რომ ცვლადის
მნიშვნელობა ჩავსვათ იმ ადგილას განვათავსებთ "კლაკნილ ფრჩხილებს '{}' "ხოლო პრჭყალების გარეთ განვათავსებთ
format ფუნქციას რომელშიც ჩავწერთ ცვლადებს და შემდეგ 'format' ფუნქცია ჩასვავს ცვლადებისთვის
მინიჭებულ მნიშვნელობებს '{}'-ის მაგივრად.

f ფუნქცია უფრო მარტივია, დავწერთ წინადადების დასაწყისში რასაც ვბეჭდავთ და შემდეგ ანალოგიურად '{}' დავუწერთ, 
აქ უბრალოდ პრჭყალებში ჩავწერთ ცვლადის სახელებს.

append ფუნქცია ყოველთვის მინიჭებულ მნიშვნელობას ჩაამატებს წინადადების ბოლოში,

ხოლო insert ჩაანაცვლებს მინიჭებულ მნიშვნელობას რომელ ინდექსსაც გავუწერთ.
'''
# 3) Write a function that takes a user's name and age, and returns a welcome message formatted with an f-string.
def welcome_message(name, age):
    return f"Welcome, {name}! You are {age} years old."

# 4) Write a function that takes a first name and last name, capitalizes them, and formats them into a single string.
def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"

# 5) Create a function that takes a string, reverses it, and formats it within a sentence.
def reverse_string(sentence):
    reversed_sentence = sentence[::-1]
    return f"The reversed sentence is: {reversed_sentence}"

# 6) Write a function that takes a sentence, a word, and an index, and inserts the word into the sentence at the given index.
def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    return " ".join(words)

# 7) Write a function that takes a sentence and returns a list of words.
def sentence_to_words(sentence):
    return sentence.split()

# 8) Create a function that takes a string of comma-separated values (CSV) and returns a list of individual items.
def csv_to_list(csv_string):
    return csv_string.split(',')

# 9) Write a function that takes a paragraph and splits it into sentences based on periods.
def split_paragraph(paragraph):
    sentences = paragraph.split('.')
    return [sentence.strip() for sentence in sentences if sentence]  # Remove extra spaces and empty strings

# 10) Write a function that takes a list and an item, and appends the item to the list.
def append_item(lst, item):
    lst.append(item)
    return lst

# 11) Create a function that takes a list and a list of items, and appends each item to the original list.
def append_multiple_items(lst, items):
    lst.extend(items)
    return lst

# 12) Create a function that appends all elements of one list to another list.
def append_all_elements(list1, list2):
    list1.extend(list2)
    return list1

# 13) Write a function that takes a list, an index, and an item, and inserts the item at the specified index.
def insert_item(lst, index, item):
    lst.insert(index, item)
    return lst

# 14) Create a function that inserts an item at the beginning of a list.
def insert_at_beginning(lst, item):
    lst.insert(0, item)
    return lst

# 15) Create a function that inserts an item at the end of a list using the insert method.
def insert_at_end(lst, item):
    lst.insert(len(lst), item)  # Insert at the last index (equivalent to append)
    return lst