# ახსენით რა არის ფუნქცია და რატომ ჯობია მისი გამოყენება.
# ფუნქცია არის პროგრამირების ენის შემადგენელი ნაწილი,
# რომელიც ასრულებს გარკვეულ დავალებას და შეიძლება გამოიძახო სხვადასხვა ადგილებიდან.


# slicing და indexing დავალებები:
# 1)Get the first element from a list.
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]
print(first_element)

# 2)Get the last element from a list using negative indexing.
last_element = my_list[-1]
print(last_element)

# 3)Slice the first three elements of a list.
first_three_elements = my_list[:3]
print(first_three_elements)

# 4)Extract the last five elements from a string.
my_string = "Hello, World!"
last_five = my_string[-5:]  
print(last_five) 

# 5)Reverse a string using slicing.
reversed_string = my_string[::-1]
print(reversed_string)

# 6)Get every third element from a list - ყოველი მესამე ელემენტი სიიდან
every_third_element = my_list[::3]  
print(every_third_element) 

# 7)Split a list into two halves using slicing. - ორ ნაწილად დაყავით სია (სიის სიგრძე აიღეთ ლუწი)
half = len(my_list) // 2 
first_half = my_list[:half]
second_half = my_list[half:] 
print(first_half)
print(second_half)