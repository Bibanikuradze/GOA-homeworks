my_tuple = (10, 20, 30, 40, 50)

second_element = my_tuple[1]

last_element = my_tuple[-1]

middle_three_elements = my_tuple[1:4]

print(f"Second element: {second_element}")
print(f"Last element: {last_element}")
print(f"Middle three elements: {middle_three_elements}")

immutable_tuple = (1, 2, 3)

try:
    immutable_tuple[1] = 5
except TypeError as e:
    print(f"Error: {e}")

person = ("Alice", 25, "Engineer")

name, age, profession = person

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")

my_tuple = (10, 20, 20, 30, 10, 10)

count_10 = my_tuple.count(10)

first_index_20 = my_tuple.index(20)

print(f"Occurrences of 10: {count_10}")
print(f"First occurrence of 20 is at index: {first_index_20}")

my_set = {1, 2, 3, 4, 5}

my_set.add(6)

my_set.remove(3)

is_present = 4 in my_set

print(f"Updated set: {my_set}")
print(f"Is 4 present in the set? {is_present}")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2

intersection_set = set1 & set2

difference_set = set1 - set2

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference (set1 - set2): {difference_set}")

my_list = [1, 2, 3, 2, 4, 1, 5, 3]

unique_set = set(my_list)

unique_list = list(unique_set)

print(f"List after removing duplicates: {unique_list}")