'''
საკლასო დავალება:
შექმენით tuple სადაც შეინახება 10 ელემენტი.
დაბეჭდეთ თითოუელი ელემენტი, ინდექსების გამოყენებით 
'''
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

for i in range(len(my_tuple)):
    print(f"Element at index {i}: {my_tuple[i]}")



'''
საკლასო დავალება:
შექმენით ფუნქცია სახელად no_duplicates, რომელსაც გადაეცემა ერთი პარამეტრი - user_list.
user_list-ის მონაცემთა ტიპია სია, ხოლო თქვენი დავალებაა რომ ფუნქციამ დააბრუნოს ეს სია იმ სახით,
რომ მასში დუპლიკატები არ გვქონდეს. 
ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით
'''
def no_duplicates(user_list):
    return list(set(user_list))

result1 = no_duplicates([1, 2, 2, 3, 4, 4, 5])
result2 = no_duplicates([10, 10, 20, 30, 30, 40])
result3 = no_duplicates(["apple", "banana", "apple", "cherry", "banana"])

print(result1)
print(result2)
print(result3)